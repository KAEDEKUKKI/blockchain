import hashlib
import json
import time

class Blockchain(object):
    """docstring for Blockchain."""

    def __init__(self,chain):
        self.chain = chain
        self.curr_data = []

    def addNewBlock(self, proof, prevhash=None):
        block = {
            "_id": len(self.chain)+1,
            "time": time.time(),
            "proof":proof,
            "data": self.curr_data,
            "prevhash": prevhash or self.hash(self.lastBlock)
        }
        block['hash'] = self.hash(block)
        self.curr_data = []
        self.chain.append(block)
        return block

    @property
    def lastBlock(self):
        block = {
            "_id": self.chain[-1]['_id'],
            "time": self.chain[-1]['time'],
            "proof": self.chain[-1]['proof'],
            "data": self.chain[-1]['data'],
            "prevhash": self.chain[-1]['prevhash']
        }
        return block

    def addNewData(self, data):
        self.curr_data.append(data)
        #return self.lastBlock['_id']+1

    def hash(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        hex_hash = hashlib.sha256(block_string).hexdigest()
        return hex_hash

    def proof_of_work(self, lastBlock):
        last_hash = self.hash(lastBlock)
        proof = 0
        while self.valid_proof(proof, last_hash) is False:
            proof+=1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof, last_hash):
        guess = f'{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
