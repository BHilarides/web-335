// 1. Display all users in the collection
db.users.find()

// 2.Display the user with the email address jbach@me.com.
db.users.find({ email: "jbach@me.com"})

// 3. Display the user with the last name Mozart.
db.users.find({ lastName: "Mozart"})

// 4. Display the user with the first name Richard.
db.users.find({ firstName: "Richard"})

// 5. Display the user with employeeId 1010.
db.users.find({ employeeId: "1010"})