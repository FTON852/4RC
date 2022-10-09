const publicKey = document.getElementById("public_key");
const history = document.getElementById("history");
const balance = document.getElementById("balance");
const nft_gallery = document.querySelector("#nft_gallery .gallery");
const last_transaction_value = document.getElementById("last_transaction_value");
const last_nft = document.getElementById("last_nft");


const get_nft = function (id) {
    return fetch(`/api/get_nft/${id}`, {
        method: 'GET',
    }).then(function (response) {
        response.json().then(function (data) {
            last_nft.src = data.uri
            return data
        });
    })

}


fetch(`/api/transactions_history/${publicKey.value}`, {
    method: 'GET',
}).then(function (response) {
    response.json().then(function (data) {
        let token = false;
        let nft = false;
        data = data.history;
        for (let i = 0; i < data.length; i++) {
            if ((!data[i].hasOwnProperty('isError') || data[i].isError === "0") && data[i].tokenSymbol === "DRUB" && token === false) {
                last_transaction_value.textContent = "+" + data[i].value
                token = true;
            }
            if ((!data[i].hasOwnProperty('isError') || data[i].isError === "0") && data[i].tokenSymbol === "NFT" && nft === false) {
                get_nft(data[i].TokenID);
                nft = true;
            }
        }
    });
})

fetch(`/api/balance/${publicKey.value}`, {
    method: 'GET',
}).then(function (response) {
    response.json().then(function (data) {
        balance.textContent = data.coinsAmount
    });
})


fetch(`/api/balance_nft/${publicKey.value}`, {
    method: 'GET',
}).then(function (response) {
    response.json().then(function (data) {
        for (let i = 0; i < data.length; i++) {
            nft_gallery.innerHTML += `
         <li>
            <img src="${data[i].uri}" style="width: 5rem; height: 5rem;border-radius: 20px;" alt="">
            <h6 style="color: var(--bs-black); text-align: center;">NFT</h6>
        </li>
        `
        }
    });
})
