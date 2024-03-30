import basic
import json
from web3 import Web3


while True:
	text = input('X3 > ')
	if text.strip() == "": continue
	result, error = basic.run('<stdin>', text)
	print(result, error)

	if error:
		print(error.as_string())
	elif result and not isinstance(result, list):
		if len(result.elements) == 1:
			print(repr(result.elements[0])) 
		else:
			print(repr(result))
	else:
		print("web3",result, result[0].get("ABI_OF_CONTRACT"))
		with open(result[0].get("ABI_OF_CONTRACT"), 'r') as f:
			abi = json.load(f)
		W3 = Web3(Web3.HTTPProvider(result[0].get("PROVIDER")))
		contract = W3.eth.contract(address=result[0].get("CONTRACT_ADDRESS"), abi=abi)
		transaction = contract.functions.setData(str(result[1][0]), str(result[1][1]), str(result[1][2]), str(result[1][3]), str(result[1][4]), str(result[1][5]), str(result[1][6]), str(result[1][7]), int(result[1][8]), str(result[1][9]), result[1][10]).build_transaction({
			'chainId': 80001,  # Polygon chain ID
			'from': "0xECcF626e4bD9f685e2F7763121CE75619D0675bb",
			'gas': 2100000,  # Adjust gas limit accordingly
			'gasPrice': W3.to_wei('50', 'gwei'),
			'nonce': W3.eth.get_transaction_count("0xECcF626e4bD9f685e2F7763121CE75619D0675bb")
      	})
		signed_tx = W3.eth.account.sign_transaction(transaction, result[0].get("PRIVATE_KEY"))
		tx_hash = W3.eth.send_raw_transaction(signed_tx.rawTransaction)
		tx_receipt = W3.eth.wait_for_transaction_receipt(tx_hash)
		if result[2].get('ack',''):
			print(tx_receipt)