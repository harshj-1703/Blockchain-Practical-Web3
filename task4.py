# 4) Write a python script to generate 2 wallet (address & private key).

from web3 import Web3
from eth_account import Account

#using mainnet
eth = "https://mainnet.infura.io/v3/cc73bc9930e94fd49e2a0b0eddbf26e2"

web3 = Web3(Web3.HTTPProvider(eth))
print(web3.is_connected())

# function to generate wallet with inputed number
def generate_wallets(num_wallets=2):
    wallets = []
    for _ in range(num_wallets):
        account = Account.create()

        address = account.address
        private_key = account._private_key.hex()

        wallets.append({
            "address": address,
            "private_key": private_key
        })

    return wallets

#number
num_wallets_to_generate = 2
#call function
generated_wallets = generate_wallets(num_wallets_to_generate)

for i, wallet in enumerate(generated_wallets, start=1):
    print("Wallet ",i)
    print("Address: ",wallet['address'])
    print("Private Key:",wallet['private_key'])