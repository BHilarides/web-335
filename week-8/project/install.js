// whatABook-install.js

// Drop and recreate the database
db.dropDatabase()

// Create collections
db.createCollection("books")
db.createCollection("customers")

// Insert documents into the books collection
db.books.insertMany([
  {
    bookId: 1001,
    title: "Pride and Prejudice",
    author: "Jane Austen",
    genre: "Romance"
  },
  {
    bookId: 1002,
    title: "1984",
    author: "George Orwell",
    genre: "Dystopian"
  },
  {
    bookId: 1003,
    title: "To Kill a Mockingbird",
    author: "Harper Lee",
    genre: "Fiction"
  },
  {
    bookId: 1004,
    title: "The Great Gatsby",
    author: "F. Scott Fitzgerald",
    genre: "Classic"
  }
])

// Insert customer with wishlist
db.customers.insertOne({
  customerId: 1,
  firstName: "Alice",
  lastName: "Johnson",
  wishlist: [
    {
        bookId: 1001,
        title: "Pride and Prejudice",
        author: "Jane Austen",
        genre: "Romance"
      },
      {
        bookId: 1003,
        title: "To Kill a Mockingbird",
        author: "Harper Lee",
        genre: "Fiction"
      }
    ]
  })