import hashlib
import datetime


class Block:

    def __init__(self, data, previous_hash=0):

        self.timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S %m-%d-%y")
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):

        sha = hashlib.sha256()


        hashStr = self.data.encode('utf-8')

        # Feed encoded byte-like object to sha
        sha.update(hashStr)


        return sha.hexdigest()

    def __repr__(self):
        a = ''
        a += "Timestamp: " + self.timestamp + "\n"
        a += "Data: " + self.data + "\n"
        a += "SHA256 Hash: " + str(self.hash) + "\n"
        a += "Previous Hash: " + str(self.previous_hash) + "\n"
        return a


class BlockChain:

    def __init__(self):
        self.blockchain = []
        self.length = 0

    def addBlock(self, data=None):

        # Edge case
        if data is None:
            print("Can't add block without data")
            return

        #  adding the first block
        if self.length == 0:
            block = Block(data, 0)
        else:
            block = Block(data, self.blockchain[self.length - 1].hash)

        self.blockchain.append(block)
        self.length += 1

    def __repr__(self):

        # Edge case
        if len(self.blockchain) == 0:
            return "Blockchain empty"

        a = ''
        for j in range(len(self.blockchain)):
            a += "Block " + str(j) + "\n"
            a += str(self.blockchain[j]) + "\n"
        return a


blockchain = BlockChain()




blockchain.addBlock("0")
blockchain.addBlock("1")
blockchain.addBlock("2")
print(blockchain)