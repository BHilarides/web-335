// whatABook-queries.js

db.books.find()

db.books.find({ genre: "Romance" })

db.books.find({ author: "Jane Austen" })

db.books.find({ bookId: 1003 })

db.customers.find(
  { customerId: 3 },
  { firstName: Jimmy, lastName: Brown, wishlist: 1 }
)