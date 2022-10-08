import requests
from api.exceptions import FailedRequestError, BadRequestStatus
from datetime import datetime as dt
from json import JSONDecodeError
from api.utils import ENDPOINT
from api.helpers import convert_var_to_dict
from api.utils.enum import GET, POST


class CoreManager:
    def __init__(self, public_key, private_key, endpoint, timeout):
        self.public_key = public_key
        self.private_key = private_key
        self.endpoint = endpoint
        self.client = requests.Session()
        self.timeout = timeout

    def _request(self, method, url, req_params):
        settings = {
            GET: self.client.prepare_request(requests.Request(method=method, url=url, params=req_params)),
            POST: self.client.prepare_request(requests.Request(method=method, url=url, data=req_params)),
        }
        if not (req := settings.get(method)):
            raise Exception(f"Invalid request method: {method}")

        try:
            response = self.client.send(req, timeout=self.timeout)
        except (
                requests.exceptions.Timeout,
                requests.exceptions.SSLError,
                requests.exceptions.ConnectionError
        ) as e:
            raise FailedRequestError(
                response=f"{method} {url}",
                params=req_params,
                message=e,
                time=dt.utcnow().strftime("%H:%M:%S")
            )
        try:
            res = response.json()
        except JSONDecodeError as e:
            raise FailedRequestError(
                response=f'{method} {url}',
                params=req_params,
                message='Conflict. Could not decode JSON.',
                time=dt.utcnow().strftime("%H:%M:%S")
            )
        if response.status_code != 200:
            raise BadRequestStatus(
                response=f"{method} {url}",
                params=req_params,
                message=response.text,
                status_code=response.status_code,
                time=dt.utcnow().strftime("%H:%M:%S")
            )
        # print(res)
        return res

    def _prepare_request(self, method=None, url=None, query=None):
        return self._request(method, url, query)


class Core(CoreManager):
    def __init__(self, public_key="", private_key="", endpoint=ENDPOINT, timeout=5):
        super().__init__(public_key=public_key, private_key=private_key, endpoint=endpoint, timeout=timeout)
        if public_key == "" or private_key == "":
            self.public_key, self.private_key = self.new_wallet()

    @property
    def balance(self):
        return self._balance()

    @property
    def balance_nft(self):
        return self._balance_nft()

    def _prepare_request(self, method=None, url=None, query=None, public=False, auth=False):
        if query:
            if auth:
                query["fromPrivateKey"] = self.private_key
            if public:
                query["toPublicKey"] = self.public_key

        return self._request(method, url, query)

    def new_wallet(self):
        path = "/v1/wallets/new"
        return self._prepare_request(
            method=POST,
            url=self.endpoint + path,
        ).values()

    def send_matic(self, toPublicKey: str, amount: float):
        query = convert_var_to_dict(locals())
        path = "/v1/transfers/matic"

        return self._prepare_request(
            method="POST",
            url=self.endpoint + path,
            query=query,
            auth=True,
        )

    def send_ruble(self, toPublicKey: str, amount: float):
        query = convert_var_to_dict(locals())
        path = "/v1/transfers/ruble"

        return self._prepare_request(
            method="POST",
            url=self.endpoint + path,
            query=query,
            auth=True,
        )

    def send_nft(self, toPublicKey: str, tokenId: int):
        query = convert_var_to_dict(locals())
        path = "/v1/transfers/nft"

        return self._prepare_request(
            method="POST",
            url=self.endpoint + path,
            query=query,
            auth=True,
        )

    def check_transaction(self, transactionHash: str):
        query = convert_var_to_dict(locals())
        path = "/v1/transfers/status/{transactionHash}".format(**query)

        return self._prepare_request(
            method=GET,
            url=self.endpoint + path,
            query=query,
        )

    def _balance(self):
        path = f"/v1/wallets/{self.public_key}/balance"

        return self._prepare_request(
            method=GET,
            url=self.endpoint + path,
        )

    def _balance_nft(self):
        path = f"/v1/wallets/{self.public_key}/nft/balance"

        return self._prepare_request(
            method=GET,
            url=self.endpoint + path,
        )

    def new_nft(self, uri: str, nftCount: int):
        query = convert_var_to_dict(locals())
        path = "/v1/nft/generate"

        return self._prepare_request(
            method="POST",
            url=self.endpoint + path,
            public=True,
            query=query,
        )

    def get_nft(self, tokenId: int):
        query = convert_var_to_dict(locals())
        path = "/v1/nft/{tokenId}".format(**query)

        return self._prepare_request(
            method=GET,
            url=self.endpoint + path,
            query=query,
        )

    def check_nft(self, transactionHash: str):
        query = convert_var_to_dict(locals())
        path = "/v1/nft/generate/{transactionHash}".format(**query)

        return self._prepare_request(
            method=GET,
            url=self.endpoint + path,
            query=query,
        )

    def transactions_history(self, page: int = 1, offset: int = 20, sort: str = "asc"):
        query = convert_var_to_dict(locals())
        path = f"/v1/wallets/{self.public_key}/history"

        return self._prepare_request(
            method=POST,
            url=self.endpoint + path,
            query=query,
        )
