from web3 import Web3

eth = "https://sepolia.infura.io/v3/cc73bc9930e94fd49e2a0b0eddbf26e2"

web3 = Web3(Web3.HTTPProvider(eth))

print(web3.is_connected())