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

# Call the find function to display all users in collection; use projections to only show first and last name
for user in db.users.find({}, {"firstName": 1, "lastName": 1}):
    print(user)
