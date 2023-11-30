#Write a python script to check balance of specified wallet using web3.py module. Take any wallet from etherscan.io

from web3 import Web3

#using mainnet
eth = "https://mainnet.infura.io/v3/cc73bc9930e94fd49e2a0b0eddbf26e2"

web3 = Web3(Web3.HTTPProvider(eth))
print(web3.is_connected())

balance1 = web3.eth.get_balance('0x690B9A9E9aa1C9dB991C7721a92d351Db4FaC990')
balance2 = web3.eth.get_balance('0xcDB43A5f2a67F67F562C1e6C4ECd7306f0F4fad1')

## Convert balances from Wei to Ether using math equation getting eth
print("Balance1 : ",balance1 / 10**18)
## Convert balances from Wei to Ether using library getting eth
print("Balance2 : ",web3.from_wei(balance2,'ether'))