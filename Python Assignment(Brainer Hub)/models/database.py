# ______This file is configure the MongoDB to store the data________

# here I am using pymongo to configure my MongoDB atlas database
from pymongo import MongoClient

# ______________________________________________________________
# this credentials can be changed easily from here
username = "ksubham789"
password = "Tesla132"

client = MongoClient(f'mongodb+srv://{username}:{password}@cluster0.vfkl0dt.mongodb.net/?retryWrites=true&w=majority')
# creating the database
db = client['PythonAssignment']
# creating the entities
companyDb = db["Company"]
employeeDb = db["Employee"]
