"""
Title: hilarides_usersp2.py
Author: Ben Hilarides
Date: 9.28.25
Description: Hands-on 5.2
"""

# Import the MongoClient
from pymongo import MongoClient
import datetime
import pprint

# Build a connection string to connect to client
client = MongoClient("mongodb+srv://web335_admin:J14M7AFCWMF0Hc5D@bellevueuniversity.qvr6m2e.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity")
print(client)

# Configure a variable to access the database
db = client['test']


# Create a new user document and added it to the users collection
hayden = {
"firstName": "Hayden",
"lastName": "Christiansen",
"employeeId": "1013",
"email": "vader@me.com",
"dateCreated": datetime.datetime.utcnow()
}

# Insert the new user document into the users collection
hayden_user_id = db.users.insert_one(hayden).inserted_id
print(hayden_user_id)

# Prove the insert worked by searching the collection for the document
print(db.users.find_one({"employeeId": "1013"}))

# Create an update query to change the user's email address
db.users.update_one(
    {"employeeId": "1013"},
    {
        "$set": {
            "email": "anakin.vader@me.com"
        }
    }
)

# Prove the update worked by searching the collection for the user by employeeId
print(db.users.find_one({"employeeId": "1013"}))

# Build a delete query to remove the user from the collection
db.users.delete_one({"employeeId": "1013"})

# Display the results of the query
# print(result)

# Prove the delete worked by searching the collection for the user by employeeId
print(db.users.find_one({"employeeId": "1013"}))