from web3 import Web3
import json

# Connect to the Ethereum node
web3 = Web3(Web3.HTTPProvider('https://polygon-mumbai.g.alchemy.com/v2/K59YdNGK95akCLJrA1m9nYPZ7JYNa8Me'))

print(web3.is_connected())
# Load contract ABI
with open('C:/Users/nagip/OneDrive/Desktop/X3/Solidity/new_contract_abi.json', 'r') as f:
    abi = json.load(f)

# Contract address
contract_address = '0xA35725FfEfebF41B667167D0fd124cd43b59CC09'

# Set up contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)

# Wallet private key
private_key = '6c2a1c294e30f4990fdc7735e92c69d232e756f70a8234a01343b571fa05c05e'  # Replace with your private key

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
transaction = contract.functions.setData(
    "lex",
    "tokens",
    "full_code",
    "ast",
    "parser",
    "result",
    "context",
    "symbol_table",
    execution_time,
    "result_value",
    "0xECcF626e4bD9f685e2F7763121CE75619D0675bb",
).build_transaction({
    'chainId': 80001,  # Polygon chain ID
    'from': "0xECcF626e4bD9f685e2F7763121CE75619D0675bb",
    'gas': 2100000,  # Adjust gas limit accordingly
    'gasPrice': web3.to_wei('50', 'gwei'),
    'nonce': web3.eth.get_transaction_count("0xECcF626e4bD9f685e2F7763121CE75619D0675bb")
})

# Sign the transaction
signed_tx = web3.eth.account.sign_transaction(transaction, private_key)

# Send the transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

# Wait for transaction receipt
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

# Print transaction receipt
print("Transaction receipt:", tx_receipt)
