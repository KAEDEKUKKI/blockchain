from blockchain import Blockchain
from holo import Hololive

def get_database():
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    import pymongo

    client = MongoClient('localhost', 27017, username='admin', password='admin')

    db = client['blockchain']

    # Create the database for our example (we will use the same database throughout the tutorial
    return db['chains']

def mine(blockchain):
    last_block = blockchain.lastBlock
    proof = blockchain.proof_of_work(last_block)

    previous_hash = blockchain.hash(last_block)
    block = blockchain.addNewBlock(previous_hash)

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    data = get_database()
    chains = []
    for i in data.find():
        chains.append(i)
    blockchain = Blockchain(chains)

    while True:
        print("<1> Add Data")
        print("<2> Make Block")
        print("<3> Show Chain")
        choice = input("Choice: ")
        if choice == "1":
            vtuber_name = input("Vtuber Name:")
            blockchain.addNewData(Hololive(vtuber_name).find())
        elif choice == "2":
            #mine(blockchain)
            if blockchain.chain == []:
                block = blockchain.addNewBlock("0"*64)
            else:
                block = blockchain.addNewBlock()
            try:
                data.insert_one(block)
                print("success")
            except Exception as e:
                print(e)
        elif choice == "3":
            for i in blockchain.chain:
                print(i)
        else:
            break
