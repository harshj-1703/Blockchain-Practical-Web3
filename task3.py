#3) Write a python script to get latest block which is being generated right now for ethereum blockchain.

from web3 import Web3

#using mainnet
eth = "https://mainnet.infura.io/v3/cc73bc9930e94fd49e2a0b0eddbf26e2"

web3 = Web3(Web3.HTTPProvider(eth))
print(web3.is_connected())

latest_block_number = web3.eth.block_number
latest_block = web3.eth.get_block(latest_block_number)

print("Latest Block Number:", latest_block_number)
print("Latest Block Hash:", latest_block['hash'])
print("Timestamp:",latest_block['timestamp'])