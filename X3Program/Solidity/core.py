from web3 import Web3
import json

# Connect to the Ethereum node
web3 = Web3(Web3.HTTPProvider('https://polygon-mumbai.g.alchemy.com/v2/K59YdNGK95akCLJrA1m9nYPZ7JYNa8Me'))

print(web3.is_connected())
# Load contract ABI
with open('C:/Users/nagip/OneDrive/Desktop/X3/Solidity/simple.json', 'r') as f:
    abi = json.load(f)

# Contract address
contract_address = '0x2e38d3e77dFBFa4e61AF350D8b021834dC368601'

# Set up contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)

# Wallet private key
private_key = '9670e17a987dff3046b11123067faefb88bac64d0bf98a1062dc05ac535c71ea'  # Replace with your private key

# Set data parameters

lex = 'Sample lex'
tokens = 'Sample tokens'
full_code = 'Sample full code'
ast = 'Sample AST'
parser = 'Sample parser'
result = 'Sample result'
context = 'Sample context'
symbol_table = 'Sample symbol table'
execution_time = 1234567890
result_value = 'Sample result value'
ipfs_data = 'Sample IPFS data'


# Create the transaction
transaction = contract.functions.store(
1
).build_transaction({
    'chainId': 80001,  # Polygon chain ID
    'from': "0x1cdaA441f3aAf776FAA522d4E83752479B59218D",
    'gas': 2100000,  # Adjust gas limit accordingly
    'gasPrice': web3.to_wei('50', 'gwei'),
    'nonce': web3.eth.get_transaction_count("0x1cdaA441f3aAf776FAA522d4E83752479B59218D")
})

# Sign the transaction
signed_tx = web3.eth.account.sign_transaction(transaction, private_key)

# Send the transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

# Wait for transaction receipt
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

# Print transaction receipt
print("Transaction receipt:", tx_receipt)
