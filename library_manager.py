import json
import os
from tabulate import tabulate

FILE_NAME = 'library.txt'

def load_library():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return[]
    return []


def save_library(library):
    with open(FILE_NAME, 'w') as file:
        json.dump(library, file, indent = 4)

def add_book(library):
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    try:
        year = int(input("Enter the Year of Publication: ").strip())
    except ValueError:
        print("Invalid year. Please enter a number.")
        return 
    genre = input("Enter Genre: ").strip()
    read_input = input("Have you read this Book? (Yes/No): ").strip().lower()
    read = True if read_input == "yes" else False

    book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "Genre": genre,
        "Read": read
    }

    library.append(book)
    print(f"Book '{title}' added to the library.\n")

def remove_book(library):
    title = input("Enter the Title of the Book to remove: ").strip()
    found = False
    for book in library:
        if book["Title"].lower() == title.lower():
            library.remove(book)
            found = True
            print(f"Book '{title}' removed from the library successfully.\n")
            break
    if not found:
        print(f"Book '{title}' not found in the library.\n")

def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    if choice not in ['1', '2']:
        print("Invalid choice. Please Try Again.\n")
        return 

    keyword = input("Enter Ttile/Author: ").strip().lower()
    matching_books = []
    for book in library:
        if (choice == '1' and keyword in book["Title"].lower()) or (choice == '2' and keyword in book["Author"].lower()):
            matching_books.append(book)

    if matching_books:
        print("\nMatching Books: ")
        display_books(matching_books)
    else:
        print("No matching books found.\n")

def display_books(library):
    if not library:
        print("No books in the library.\n")
        return
    
    print("\nYour Library: ")
    display_table(library)

def display_table(books):
    table = []
    for idx, book in enumerate(books, start = 1):
        read_status = "Yes" if book["Read"] else "Unread"
        table.append([idx, book["Title"], book["Author", book["Year"], book["Genre"],read_status]])

    headers = ["#", "Title", "Author", "Year", "Genre", "Status"]
    print(tabulate(table, headers = headers, tablefmt = "fancy_grid", stralign = "center"))
    print()

def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("No books in the library.\n")
        return
    read_books = sum(1 for book in library if book["Read"])
    percentage_read = (read_books/total_books) * 100
    print(f"Total Books: {total_books}")
    print(f"Percentage of Books Read: {percentage_read:.1f}%")

def main():
    library = load_library()
    while True:
        print("------------ Menu -------------\nWelcome to your Personal library Manager!")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("Library saved to file. Bubbyeee!!!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()

