from network import Core

publicKey = "0x9c6092230F9E09f3b70242B9341187d6c8B1fA01"
privateKey = "68d03fb367f0d163bed237af3f523c5b5d6363de1d53971d5f7a35466cc72968"
new_publicKey = '0xBaD2a1448D947ED57Aa885df4Ee8f33c96A2e1D5'
new_privateKey = '63cddfcc6bc064434a0ad47449ac85acaaa4a405ebda6b32943382aece8284fd'

if __name__ == '__main__':
    network = Core(publicKey, privateKey)
    network.balance

    new_public, new_private = network.new_wallet()

    # transactionHash = network.send_matic(new_publicKey, 0.2)["transaction"]
    # network.check_transaction(transactionHash)
    #
    # transactionHash = network.send_ruble(new_public, 0.000002)["transaction"]
    # network.check_transaction(transactionHash)
    #
    # transactionHash = network.new_nft("https://i.ibb.co/WPhyscn/Image.png", 2)["transaction_hash"]
    # network.check_transaction(transactionHash)
    # network.get_nft(529)
    for i in [740,
              530,
              531,
              532,
              581,
              582,
              585,
              586,
              587,
              588,
              589,
              590,
              591,
              592,
              721,
              722,
              739,
              775,
              776,
              808,
              809,
              817,
              818,
              819,
              820,
              830,
              831,
              832,
              833,
              837,
              838,
              839,
              840,
              841,
              842,
              1113,
              1114]:
        transactionHash = network.send_nft(new_public, i)["transaction_hash"]
        # network.check_nft(transactionHash)

    network.balance_nft

    network.transactions_history()
