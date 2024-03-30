import basic
from web3 import Web3
import json

while True:
	text = input('X3 > ')
	if text.strip() == "": continue
	result, error = basic.run('<stdin>', text)
	print(result, error)

	if error:
		print(error.as_string())
	elif result and not isinstance(error, list):
		if len(result.elements) == 1:
			print(repr(result.elements[0])) 
		else:
			print(repr(result))
	else:
		with open(ABI_OF_CONTRACT, 'r') as f:
          abi = json.load(f)
		print("web3")