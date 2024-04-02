from web3 import Web3

alchemy_url = "https://polygonzkevm-mainnet.g.alchemy.com/v2/58Dm_Z3kNnpx3ALgcgv4UhM-xZlgKmkd"


w3 = Web3(Web3.HTTPProvider(alchemy_url))
# print(w3.isConnected())
print(w3.is_connected())


# {'pk':xyz, 'chain':'polygonzkevm', 'network':'mainnet', 'provider':'', 'language':''}