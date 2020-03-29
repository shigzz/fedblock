from web3 import Web3,HTTPProvider
import json

server = Web3(HTTPProvider('http://localhost:7545'))

print(server)

#CONTRACT_ADDRESS = server.toChecksumAddress("0xb495d137d3a150194ed5b78a60f7cc6ea9c8e81f")
CONTRACT_ADDRESS = server.toChecksumAddress("0x3Eba6FF915ec245a832042fFfa63D7a615384836")

print(CONTRACT_ADDRESS)

with open('../build/contracts/LearningContract.json') as f:
    voter_contract_data = json.load(f)

CONTRACT_ABI = voter_contract_data['abi']
contract = server.eth.contract(address=CONTRACT_ADDRESS,
                                           abi=CONTRACT_ABI)

print(contract)

ipfsHash = contract.Call().getCheckPointIpfsHash()

print(ipfsHash)
