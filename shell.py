import basic
import json
from web3 import Web3
import os
import time
from web3.middleware import geth_poa_middleware
from pymongo import MongoClient


CURRENT_PATH = os.getcwd()
MABI_OF_CONTRACT = os.path.join(CURRENT_PATH, 'Solidity','mnew_contract_abi.json')
ChainControl = 10
uri = "mongodb+srv://nagi:nagi@cluster0.ohv5gsc.mongodb.net/nagidb"
client = MongoClient(uri)


def do_line():
  SIZE = os.get_terminal_size()
  COL = SIZE.columns
  LINE = SIZE.lines
  print("-"*COL)

def word_line(word):
  SIZE = os.get_terminal_size()
  COL = SIZE.columns
  LINE = SIZE.lines
  actual_col = COL - len(word)
  halfofcol = actual_col / 2
  print("-"*int(halfofcol) + word + "-"*int(halfofcol))



while True:
	text = input('X3 >>> ')
	if text.strip() == "": continue
	result, error = basic.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result and not isinstance(result, list):
		if len(result.elements) == 1:
			print(repr(result.elements[0])) 
		else:
			print(repr(result))
	else:
    ############################################### For Web3 ##########################################################
		start_time = time.time()
		with open(result[0].get("ABI_OF_CONTRACT"), 'r') as f:
			abi = json.load(f)
		with open(MABI_OF_CONTRACT, 'r') as mf:
			mabi = json.load(mf)
		W3 = Web3(Web3.HTTPProvider(result[0].get("PROVIDER")))
		W3.middleware_onion.inject(geth_poa_middleware, layer=0)
		contract = W3.eth.contract(address=result[0].get("CONTRACT_ADDRESS"), abi=abi)
		transaction = contract.functions.setData(str(result[1][0]), str(result[1][1]), str(result[1][2]), str(result[1][3]), str(result[1][4]), str(result[1][5]), str(result[1][6]), str(result[1][7]), int(result[1][8]), str(result[1][9]), result[1][10]).build_transaction({
			'chainId': 80001,  # Polygon chain ID
			'from': "0xECcF626e4bD9f685e2F7763121CE75619D0675bb",
			'gas': 210000,  # Adjust gas limit accordingly
			'gasPrice': W3.to_wei('50', 'gwei'),
			'nonce': W3.eth.get_transaction_count("0xECcF626e4bD9f685e2F7763121CE75619D0675bb")
    	})
		signed_tx = W3.eth.account.sign_transaction(transaction, result[0].get("PRIVATE_KEY"))
		tx_hash = W3.eth.send_raw_transaction(signed_tx.rawTransaction)
		tx_receipt = W3.eth.wait_for_transaction_receipt(tx_hash)
		#-------------------------------------------mumbai--------------------------------------------------------
		mcontract = W3.eth.contract(address="0x9Ee6c696C197B8a25f495FF51D897fC68b31a187", abi=abi)
		data = (
			str(result[1][0]),
			str(result[1][1]),
			str(result[1][2]),
			"ast_value",
			"parser_value",
			str(result[1][5]),
			"context_value",
			"symbolTable_value",
			int(result[1][8]),
			"resultValue_value",
			result[1][10]
		)
		mtransaction = mcontract.functions.setData(*data).build_transaction({
			'chainId': 80001,  # Polygon chain ID
			'from': "0x1cdaA441f3aAf776FAA522d4E83752479B59218D",
			'gas': 1000000,  # Adjust gas limit accordingly
			'gasPrice': W3.to_wei('50', 'gwei'),
			'nonce': W3.eth.get_transaction_count("0x1cdaA441f3aAf776FAA522d4E83752479B59218D")
    	})
		msigned_tx = W3.eth.account.sign_transaction(mtransaction, "9670e17a987dff3046b11123067faefb88bac64d0bf98a1062dc05ac535c71ea")
		mtx_hash = W3.eth.send_raw_transaction(msigned_tx.rawTransaction)
		mtx_receipt = W3.eth.wait_for_transaction_receipt(mtx_hash)
		end_time = time.time()
		#-----------------------------------mumbai---------------------------------------------------

		#-----------------------------------mango----------------------------------------------------

		data = {
			"lex": result[1][0],
			"tokens": result[1][1],
			"fullCode": result[1][2],
			"ast": result[1][3],
			"parser": result[1][4],
			"result": result[1][5],
			"context": result[1][6],
			"symbolTable": result[1][7],
			"executionTime": result[1][8],
			"resultValue": result[1][9],
			"account": result[1][10],
			"type": "polygon",
			"transaction":tx_receipt
		}
		db = client.X3
		# Access a specific collection within the database
		collection = db.X3
		# Insert the document into the collection
		insert_result = collection.insert_one(data)
		# Check if the insertion was successful
		if insert_result.inserted_id:
			print("Data inserted successfully.")
		else:
			print("Failed to insert document.")

		#-----------------------------------Core----------------------------------------------------
		with open(os.path.join(CURRENT_PATH, 'Solidity',"simple.json"), 'r') as f:
			abi = json.load(f)
		contract = W3.eth.contract(address="0x2e38d3e77dFBFa4e61AF350D8b021834dC368601", abi=abi)

		transaction = contract.functions.store(
			ChainControl
		).build_transaction({
			'chainId': 80001,  # Polygon chain ID
			'from': "0x1cdaA441f3aAf776FAA522d4E83752479B59218D",
			'gas': 2100000,  # Adjust gas limit accordingly
			'gasPrice': W3.to_wei('50', 'gwei'),
			'nonce': W3.eth.get_transaction_count("0x1cdaA441f3aAf776FAA522d4E83752479B59218D")
		})
		# Sign the transaction
		signed_tx = W3.eth.account.sign_transaction(transaction, "9670e17a987dff3046b11123067faefb88bac64d0bf98a1062dc05ac535c71ea")
		# Send the transaction
		tx_hash = W3.eth.send_raw_transaction(signed_tx.rawTransaction)
		try:
			# Send the transaction
			tx_hash = W3.eth.send_raw_transaction(signed_tx.rawTransaction)
			# Wait for transaction receipt
			tx_receipt = W3.eth.wait_for_transaction_receipt(tx_hash)
		except:
			pass

		#---------------------------------------------------------------------------------------------

		# Calculate the elapsed time
		elapsed_time = end_time - start_time
		if result[2].get('ack','') or result[2].get('ackBc','') :
			do_line()
			print(tx_receipt, '\n' , mtx_receipt)
		word_line("\nExecution Details\n")
		print("Program Executed within: " + str(result[1][8])+"s","\t\t\t Blockchain Execution Time: " + str(elapsed_time))
		do_line()