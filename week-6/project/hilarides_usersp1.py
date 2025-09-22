"""
Title: hilarides_usersp1.py
Author: Ben Hilarides
Date: 9.21.25
Description: Hands-on 4.2
"""

# Import the MongoClient
from pymongo import MongoClient
import datetime

# Build a connection string to connect to client
client = MongoClient("mongodb+srv://web335_admin:J14M7AFCWMF0Hc5D@bellevueuniversity.qvr6m2e.mongodb.net/?retryWrites=true&w=majority&appName=BellevueUniversity")

print(client)

# Configure a variable to access the database
db = client['web335DB']

# Display all documents in the users collection
print("\n-- DISPLAYING USERS DOCUMENTS FROM find() QUERY --")
for doc in db.users.find():
    print(doc)

# Display document by employeeId '1011'
print("\n-- User with employeeId '1011' --")
print(db.users.find_one({"employeeId": "1011"}))

# Display user by lastName 'Mozart'
print("\n-- User with lastName 'Mozart' --")
print(db.users.find_one({"lastName": "Mozart"}))

# Close Connection
client.close()
print("\n-- Connection Closed --")
