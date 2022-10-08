from network import Core

publicKey = "0x9c6092230F9E09f3b70242B9341187d6c8B1fA01"
privateKey = "68d03fb367f0d163bed237af3f523c5b5d6363de1d53971d5f7a35466cc72968"
new_publicKey = '0x4844d1696928ca9898b8bCfFa2fa0B37dA2E2772'
new_privateKey = 'a81b46948620bb3471bc99c70850126c05dc8f3b0d7e356ba817b513d5d9ad3f'

if __name__ == '__main__':
    network = Core(publicKey, privateKey)
    network.balance

    new_public, new_private = network.new_wallet()

    transactionHash = network.send_matic(new_public, 0.2)["transaction"]
    network.check_transaction(transactionHash)

    transactionHash = network.send_ruble(new_public, 0.2)["transaction"]
    network.check_transaction(transactionHash)

    transaction_hash = network.new_nft("", 2)["transaction_hash"]
    network.get_nft(529)

    transactionHash = network.send_nft(new_public, 529)["transaction_hash"]
    network.check_nft(transactionHash)

    network.balance_nft

    network.transactions_history()


