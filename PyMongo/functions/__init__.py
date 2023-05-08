from pymongo import MongoClient

connect = MongoClient('localhost', 27017)


def updateRoll(db, collect, name, roll):
    collection = connect[db][collect]
    collection.update_many({"name": name}, {"$set": {"roll": roll}})


def deleteRecord(db, collect, name):
    collection = connect[db][collect]
    collection.delete_one({"name": name})


def insertRecord(db, collect, name, roll):
    collection = connect[db][collect]
    collection.insert_one({"name": name, "roll": roll})


def updateListener(db, collect, ):
    collection = connect[db][collect]

    cursor = collection.watch([{'$match': {'operationType': 'update'}}])

    id = []
    with cursor as stream:
        for change in stream:
            id.append(change["documentKey"]["_id"])

    return id