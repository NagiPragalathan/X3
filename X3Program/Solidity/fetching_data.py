from web3 import Web3
import json

# Connect to the Ethereum node
web3 = Web3(Web3.HTTPProvider('https://polygon-mumbai.g.alchemy.com/v2/K59YdNGK95akCLJrA1m9nYPZ7JYNa8Me'))

from web3.middleware import geth_poa_middleware

# Load contract ABI
with open('C:/Users/nagip/OneDrive/Desktop/X3/Solidity/new_contract_abi.json', 'r') as f:
    abi = json.load(f)
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Contract address
contract_address = '0xA35725FfEfebF41B667167D0fd124cd43b59CC09'

# Set up contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)

# Fetch data by ID using call()
data_by_id = contract.functions.getDataById(1).transact()

print("Data stored for ID 1:")
print("Lex:", data_by_id[0])
print("Tokens:", data_by_id[1])
print("Full Code:", data_by_id[2])
print("AST:", data_by_id[3])
print("Parser:", data_by_id[4])
print("Result:", data_by_id[5])
print("Context:", data_by_id[6])
print("Symbol Table:", data_by_id[7])
print("Execution Time:", data_by_id[8])
print("Result Value:", data_by_id[9])
print("\n")
