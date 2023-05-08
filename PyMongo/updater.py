# from pymongo import MongoClient
from time import sleep
from functions import updateRoll
#
# connect = MongoClient('localhost', 27017)
# database = connect.app1
#
# collection = database["Learn"]
# collection.delete_many({})
# data = [
#     {
#         "name": "Abhinav",
#         "roll": 5,
#         "address": {
#             "flat": 1,
#             "street": "Sarjapur",
#             "state": "Karnataka"
#         }
#     },
#     {
#         "name": "Vimal",
#         "roll": 7,
#         "address": {
#             "flat": 2,
#             "street": "MG road",
#             "state": "Karnataka"
#         }
#     },
#     {
#         "name": "Aryan",
#         "roll": 9,
#         "address": {
#             "flat": 3,
#             "street": "Outer Ring Road",
#             "state": "Karnataka"
#         }
#     }
# ]
#
# document = collection.insert_many(data)
# # result = collection.find()
iteration = 0
while True:
    if iteration % 2 == 0:
        updateRoll("app1", "Learn", "Abhinav", 0)
    else:
        updateRoll("app1", "Learn", "Abhinav", 1)
    iteration += 1
    sleep(5)
