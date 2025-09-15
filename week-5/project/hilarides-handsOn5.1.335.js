// Add a new user to the user’s collection
db.users.insertOne(
   {
     name: "Jane Doe",
     email: "janedoe@gmail.com",
     age: "29"
   }
);

// Update Update Mozart’s email address to mozart@me.com
db.users.updateOne(
   { lastName: "Mozart" },
   { $set: { email: "mozart@me.com" } }
);

// Display all users in the collection with only their first name, last name, and email address
db.users.find(
  {},
  { firstName: 1, lastName: 1, email: 1, _id: 0 }
);