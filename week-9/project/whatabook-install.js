// whatabook-install.js

// Drop and recreate database
db.dropDatabase()

// Create collections
db.createCollection("customers")
db.createCollection("books")

// Insert books
db.books.insertMany([
    {
        bookId: 1001,
        title: "The Space Between worlds",
        author: "Micaiah Johnson",
        genre: "Sci-fi",
    },
    {
        bookId: 1002,
        title: "It Ends with us",
        author: "Colleen Hoover",
        genre: "Fiction",
    },
    {
        bookId: 1003,
        title: "Onyx Storm",
        author: "Rebecca Yarros",
        genre: "Fantasy",
    },
    {
        bookId: 1004,
        title: "The Last Thing He Told Me",
        author: "Laura Dave",
        genre: "Mystery",
    },
    {
        bookId: 1005,
        title: "The Midnight Library",
        author: "Matt Haig",
        genre: "Fiction",
    },
    {
        bookId: 1006,
        title: "Project Hail Mary",
        author: "Andy Weir",
        genre: "Sci-fi",
    }
])


// Insert customers
db.customers.insertMany([
    {
        customerId: "c102",
        firstName: "Mark",
        lastName: "Whalberg",
        wishlist: [
            {
                bookId: 1002,
                title: "It Ends with us",
                author: "Colleen Hoover",
                genre: "Fiction",
            }
        ]
    },
    {
        customerId: "c103",
        firstName: "Donny",
        lastName: "Whalberg",
        wishlist: [
            {
                bookId: 1003,
                title: "Onyx Storm",
                author: "Rebecca Yarros",
                genre: "Fantasy",
            }
              ]
    },
    {
        customerId: "c104",
        firstName: "Willem",
        lastName: "Dafoe"
    },
    {
        customerId: "c105",
        firstName: "Robert",
        lastName: "DeNiro"
    },
    {
        customerId: "c106",
        firstName: "Al",
        lastName: "Pacino"
    }
])

print("Database setup complete!")
print("Books inserted: ", db.books.countDocuments({}))
print("Customers inserted: ", db.customers.countDocuments({}))