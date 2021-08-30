import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]  # Create a database called "mydatabase"

#print(myclient.list_database_names()) # Return a list of your system's databases

'''dblist = myclient.list_database_names()
if "mydatabase" in dblist:
print("The database exists.") #Check if "mydatabase" exists'''

mycol = mydb["customers"] #Create a collection called "customers"

mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict) #inserting a record or document into collection
print(x.inserted_id) #return the value of _id field