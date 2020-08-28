import pymongo

# Generic constants
STATUS = 'status'
SUCCESS = 'success'
ERROR = 'error'
DATA = 'data'

#Creating DB
mongo_uri="mongodb+srv://admin:admin123@biznet.na8h3.gcp.mongodb.net/referralAPI?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_uri)
mydb = client["referralAPI"]    

