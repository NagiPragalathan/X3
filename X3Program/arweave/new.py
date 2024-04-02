import arweave


wallet_file_path = "C:/Users/nagip/OneDrive/Desktop/X3/arweave/NLCO2XVEVZ36UFDd6puhVMBTLdjzgfw-tzt1qEjFMz0.json"
wallet = arweave.Wallet(wallet_file_path)

balance =  wallet.balance

last_transaction = wallet.get_last_transaction_id()
print(balance, last_transaction)


transaction = arweave.Transaction(wallet, quantity=0.3, to='JLbGnMyKGNTgyo1lWtTLC6Jooy_LbHMGlMUE5uglQuY')
transaction.sign()
transaction.send()
