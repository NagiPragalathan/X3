from web3 import Web3

# Connect to the Ethereum node
w3 = Web3(Web3.HTTPProvider('https://polygon-mumbai.g.alchemy.com/v2/mn-3ohp2vXDjCM0jyeRq7J0shVhblg-l'))  # Connect to your Ethereum node URL

# Set the contract address and ABI
contract_address = "0xContractAddress"
abi = [
    {
        "inputs": [
            {"internalType": "string", "name": "_lex", "type": "string"},
            {"internalType": "string", "name": "_tokens", "type": "string"},
            {"internalType": "string", "name": "_fullCode", "type": "string"},
            {"internalType": "string", "name": "_ast", "type": "string"},
            {"internalType": "string", "name": "_parser", "type": "string"},
            {"internalType": "string", "name": "_result", "type": "string"},
            {"internalType": "string", "name": "_context", "type": "string"},
            {"internalType": "string", "name": "_symbolTable", "type": "string"},
            {"internalType": "uint256", "name": "_executionTime", "type": "uint256"},
            {"internalType": "string", "name": "_resultValue", "type": "string"},
            {"internalType": "address", "name": "user_address", "type": "address"},
        ],
        "name": "setData",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    }
]

# Create contract instance
contract = w3.eth.contract(address=contract_address, abi=abi)

# Define the data to be passed to the contract function
data = (
    "lex_value",
    "tokens_value",
    "fullCode_value",
    "ast_value",
    "parser_value",
    "result_value",
    "context_value",
    "symbolTable_value",
    123456,
    "resultValue_value",
    "0x1cdaA441f3aAf776FAA522d4E83752479B59218D"
)

# Call the contract function
mtransaction = contract.functions.setData("str(result[1][0])", "str(result[1][1])", "str(result[1][2])", "str(result[1][3])", "str(result[1][4])", "str(result[1][5])", "str(result[1][6])", "str(result[1][7])", 1," str(result[1][9])", "0x1cdaA441f3aAf776FAA522d4E83752479B59218D").build_transaction({
	'chainId': 80001,  # Polygon chain ID
	'from': "0x1cdaA441f3aAf776FAA522d4E83752479B59218D",
	'gas': 210000,  # Adjust gas limit accordingly
	'gasPrice': w3.to_wei('50', 'gwei'),
	'nonce': w3.eth.get_transaction_count("0x1cdaA441f3aAf776FAA522d4E83752479B59218D")
})

# Wait for transaction receipt
receipt = w3.eth.wait_for_transaction_receipt(mtransaction)
print(receipt)
