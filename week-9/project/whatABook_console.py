"""
Title: whatABook_console.py
Author: Mariea Nies, Ben Hilarides
Date: 10.9.25
Description: WhatABook Bulldogs Edition

Code Attribution: MongoDB connection and error handling patterns adapted from PyMongo documentation
https://pymongo.readthedocs.io/en/stable/tutorial.html#connecting-to-mongodb
URL encoding for MongoDB credentials using urllib.parse.quote_plus
https://www.mongodb.com/docs/languages/python/pymongo-driver/v4.8/security/authentication/x509/
Database query patterns and cursor handling from MongoDB Python Driver documentation
https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html
Console menu structure inspired by common CLI application designs
https://dribbble.com/tags/cli
Error handling for ConnectionFailure and ServerSelectionTimeoutError from PyMongo best practices
https://pymongo.readthedocs.io/en/stable/api/pymongo/errors.html
"""

# Import the MongoClient
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
import sys
from urllib.parse import quote_plus

# Build a connection string to connect to client
def connect_to_database():
  '''
  Establishes connection to MongoDB cluster.

  Returns:
    db: MongoDB database object for 'WhatABook' database.

  Raises:
    ConnectionFailure: If unable to connect to MongoDB server.
    ServerSelectionTimeoutError: If server selection times out.

  Attribution: Connection pattern adapted from PyMongo documentation.
  '''
  try:

    # Properly encode password to handle special characters
    # Attribution: URL encoding pattern from urllib.parse.documentation https://docs.python.org/3/library/urllib.parse.html

    username = "web335_admin"
    password = "J14M7AFCWMF0Hc5D"
    cluster = "bellevueuniversity.qvr6m2e.mongodb.net"

    uri = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=BellevueUniversity"
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)

    # Test the connection
    client.admin.command('ping')
    print("Connected to MongoDB successfully!")

    # Configure a variable to access the database
    db = client['WhatABook']
    return db
  except (ConnectionFailure):
    print("Failed to connect to MongoDB. Please check connection string and network connectivity.")
    sys.exit(1)
  except (ServerSelectionTimeoutError):
    print("Server selection timed out. Please ensure the MongoDB server is reachable.")
    sys.exit(1)
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)

# Display a list of all books in the collection
def display_all_books(books_collection):
  '''
  Retrieves and displays all books from the 'books' collection.

  Attribution: MongoDB find() query pattern from PyMongo documentation.
    Python enumerate() function for indexing from Python standard library
    https://docs.python.org/3/library/functions.html#enumerate
    Python len() function for counting items from Python standard library
    https://docs.python.org/3/library/functions.html#len
  '''
  print("\n" + "-" * 65)
  print("\n  -- DISPLAYING all BOOKS in our database --")
  print("-" * 65)

  all_books = books_collection.find({})

  if not all_books:
    print("No books found in our database!")
  else:
    for i, book in enumerate(all_books, 1):
      print(f"{i}. {book.get('title', 'Unknown Title')}")
      print(f"  Author: {book.get('author', 'Unknown Author')}")
      print(f"  Genre: {book.get('genre', 'Unknown Genre')}")
      print(f"  Book ID: {book.get('bookId', 'Unknown ID')}")
    print(f"\nTotal books found: {len(list(all_books))}")
  print("-" * 65)

# Display a list of books by genre

def display_books_by_genre(books_collection):
    print("\n" + "-" * 65)
    print("\n  -- DISPLAYING BOOKS by GENRE --")
    print("-" * 65)

    # Get all genres from the collection
    genres = books_collection.distinct("genre")

    if not genres:
        print("No genres found in our database!")
        return

    # Display Genre Options
    # Attribution: F Strings https://docs.python.org/3/reference/lexical_analysis.html#f-strings
    print("\nAvailable Genres:")
    for i, genre in enumerate(genres, 1):
        print(f"{i}. {genre}")

    # Prompt user to select a genre
    try:
        choice = input("\nSelect a genre by number (or 'q' to go back): ").strip()

        if choice.lower() == 'q':
            return

        choice_num = int(choice)

        if 1 <= choice_num <= len(genres):
            selected_genre = genres[choice_num - 1]

            # Find books in the selected genre
            books_in_genre = list(books_collection.find({"genre": selected_genre}))

            print(f"\n--- Books in Genre: '{selected_genre}' genre ---")
            if books_in_genre:
                for i, book in enumerate(books_in_genre, 1):
                    print(f"{i}. {book.get('title', 'Unknown Title')}")
                    print(f"  Author: {book.get('author', 'Unknown Author')}")
                    print(f"  Book ID: {book.get('bookId', 'Unknown ID')}")
                print(f"\nTotal books found in '{selected_genre}': {len(books_in_genre)}")
            else:
                print(f"No books found in the '{selected_genre}' genre.")
        else:
            print("Invalid selection. Please choose a valid genre number.")
    # Basic error handling
    # Attribution: https://docs.python.org/3/tutorial/errors.html#handling-exceptions
    except ValueError:
        print("Invalid input. Please enter a number corresponding to a genre.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print("-" * 65)

# Display a users wishlist by customerId
def display_customer_wishlist(customers_collection):
  '''
  Retrieves and displays a customer's wishlist by their customerId.
  Args:
    customers_collection: The MongoDB collection object for 'customers'.
  Attribution: MongoDB find_one() query pattern from PyMongo documentation.
  '''
  print("\n" + "-" * 65)
  print("\n  -- DISPLAYING CUSTOMER WISHLIST --")
  print("-" * 65)

  # Get all available customer IDs from database
  # Attribution: https://docs.python.org/3/tutorial/datastructures.html
  all_customers = list(customers_collection.find({}, {"customerId": 1, "firstName":1, "lastName": 1}))

  if not all_customers:
    print("\n Error: No customers found in the database! ")
    print("-" * 65)
    return

  # Display available customer IDs
  print("\n" + "=" * 65)
  print("\nAvailable Customer IDs:")
  print("=" * 65)

  valid_customer_ids = []
  for customer in all_customers:
    cust_id = customer.get("customerId", "Unknown ID")
    first_name = customer.get("firstName", "Unknown First Name")
    last_name = customer.get("lastName", "Unknown Last Name")

    # Remove 'c' prefix for display
    # Attribution: String manipulation from Python standard library https://docs.python.org/3/library/string.html
    display_id = cust_id[1:] if cust_id.startswith('c') else cust_id
    print(f"  ID: {display_id} - {first_name} - {last_name}")
    valid_customer_ids.append(cust_id)
  print("=" * 65)

  # Prompt user for customerId
  customer_id_input = input("\nEnter a Customer ID to view their wishlist (or 'q' to go back): ").strip()

  # Add 'c' prefix if missing
  customer_id = f"c{customer_id_input}" if not customer_id_input.startswith('c') else customer_id_input

  # Basic error handling for invalid customerId input
  if customer_id not in valid_customer_ids:
    print(f"\n Error: Customer ID '{customer_id_input}' not found. Please us one of the available Customer IDs. ")
    print("-" * 65)
    return

  # Find the customer document by customerId
  customer = customers_collection.find_one({"customerId": customer_id})

  if customer:
    print(f"\n --- Wistlist for {customer.get('firstName', '')} {customer.get('lastName', '')} (ID: {customer_id} --- ")

    wishlist = customer.get('wishlist', [])

    if wishlist:
      for i, book_id in enumerate(wishlist, 1):
        print(f"\n{i}, {book_id.get('title', 'Unknown Title')}")
        print(f"  Author: {book_id.get('author', 'Unknown Author')}")
        print(f"  Genre: {book_id.get('genre', 'Unknown Genre')}")
        print(f"  Book ID: {book_id.get('bookId', 'Unknown ID')}")
      print(f"\nTotal books in wishlist: {len(wishlist)}")
    else:
      print("\nThis Customer's Wishlist is empty.")
  else:
    print(f"\n Error: Customer ID '{customer_id_input}' not found in the database! ")
    print("The customer may not exist in database.")

  print("-" * 65)

def display_menu():
  """
  Displays the main menu options to the user.
  Attribution: Console menu structure inspired by common CLI application designs
  https://dribbble.com/tags/cli
  """
  print("\n" + "=" * 65)
  print("  -- WhatABook Bulldogs Edition: Main Menu --")
  print("=" * 65)
  print("1. Display All Books")
  print("2. Display Books by Genre")
  print("3. Display Customer Wishlist")
  print("4. Exit Program")
  print("=" * 65)

# Main function to run the console application
def main():
  db = connect_to_database()
  books_collection = db['books']
  customers_collection = db['customers']

  # Main program loop
  while True:
    display_menu()
    choice = input("Enter your choice (1-4): ").strip()

    if choice == '1':
      display_all_books(books_collection)
    elif choice == '2':
      display_books_by_genre(books_collection)
    elif choice == '3':
      display_customer_wishlist(customers_collection)
    elif choice == '4':
      print("\nThank you for using WhatABook! Goodbye!")
      break
    else:
      print("Invalid choice. Please select a valid option (1-4).")

    input("\nPress Enter to continue...")

if __name__ == "__main__":
  main()