from web3 import Web3
import json

# Connect to the Ethereum node
web3 = Web3(Web3.HTTPProvider('https://polygonzkevm-mainnet.g.alchemy.com/v2/58Dm_Z3kNnpx3ALgcgv4UhM-xZlgKmkd'))

# Load contract ABI
with open('C:/Users/nagip/OneDrive/Desktop/X3/Solidity/DataStorageABI.json', 'r') as f:
    abi = json.load(f)

# Contract address
contract_address = '0x771F6344205A597664EC296FCE0EE8CB6d1F58c2'

# Set up contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)

# Wallet private key
private_key = '6c2a1c294e30f4990fdc7735e92c69d232e756f70a8234a01343b571fa05c05e'

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

# Send transaction to add data
tx_hash = contract.functions.setData(
    lex,
    tokens,
    full_code,
    ast,
    parser,
    result,
    context,
    symbol_table,
    execution_time,
    result_value,
    ipfs_data
).transact({
    'from': web3.eth.accounts[0],
    'gas': 1000000,  # Adjust gas limit accordingly
    'gasPrice': web3.toWei('50', 'gwei')
})

# Wait for transaction receipt
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Print transaction receipt
print(tx_receipt.contractAddress)
print("Transaction receipt:", tx_receipt)
