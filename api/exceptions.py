class FailedRequestError(Exception):
    def __init__(self, response, params, message, time):
        self.response = response
        self.params = params
        self.message = message
        self.time = time
        super().__init__(self.message)

    def __str__(self):
        return f'{self.response}\n' \
               f'Params: {self.params}\n' \
               f'Message: {self.message}\n' \
               f'Time: {self.time}'


class BadRequestStatus(Exception):
    def __init__(self, response, params, message, status_code, time):
        self.response = response
        self.params = params
        self.message = message
        self.status_code = status_code
        self.time = time

    def __str__(self):
        return f'{self.response}\n' \
               f'Params: {self.params}\n' \
               f'Message: {self.message}\n' \
               f'Status Code: {self.status_code}\n' \
               f'Time: {self.time}'
