#Group Project 4 
#version 1.0
#Authors: Grace, Leona, Jose, Mahdi
#Library Book cataloug system
#Purpose: Design a library book catalog system that will implement the following features;
#storing and loading books information into/from a file.
#Searching for a book.
#Borrowing a book.
#Returning a book.
#Adding a new book.
#Removing a book.
#Displaying a list of books.
#Saving the book catalog.

from book import Book

# loading a list of books from a file
def load_books(): #Grace
    book_list = []
    book_count = 0
    catalouge = open('code/books.csv', 'r')
    for line in catalouge:
        items = line.rstrip('\n').split(',')
        isbn = items[0]
        title = items[1]
        author = items[2]
        genre = int(items[3])
        availability = bool(items[4])
        bookCreated = Book(isbn, title, author, genre, availability)
        book_list.append(bookCreated)
        book_count += 1
    catalouge.close()    
    return book_list 

#printing the options menu
def print_menu(): #Leona
    library_menu = {0:"Exit the system", 1: "Search for a book", 2: "Borrow a book", 3: "Return a book"}
    print("Welcome to the Library\n")
    print(f"1. {library_menu.get(1)}")
    print(f"2. {library_menu.get(2)}")
    print(f"3. {library_menu.get(3)}")
    print(f"0. {library_menu.get(0)}\n")    
    selection = int(input("Enter your selection: "))
    if selection not in library_menu.keys():
        print("Invalid option. Please try again.")
        print_menu()
    return selection

#searching for a book
def search_books(self, book_list): #Grace
    search_result=[]
    print("-- Search for books --")
    search_input = input("Enter Search Value: ")
    for book_item in book_list:
        genre= str(book_item.get_genre_name())
        if search_input.lower() in book_item.get_isbn().lower() \
            or search_input.lower() in book_item.get_title().lower() \
            or search_input.lower() in book_item.get_author().lower() \
            or search_input.lower() in genre.lower():
            search_result.append(book_item)
    if len(search_result) == 0:
        print("No matching books found.")
    else:
        self.print_books(search_result)

#borrowing a book
def borrow_book(book_list): #Leona
    #should work but need to be tested once find book is programmed 
    borrow_isbn = int(input("Enter a book ISBN: "))
    book = find_book_by_isbn(borrow_isbn)
    if book is not None:
        print("Book has been borrowed")
        Book.borrow_it()
    else:
        print("Book not found")

#finding a book by ISBN
def find_book_by_isbn(book_list): #Grace
    
    if Book.isbn in book_list:
        return Book

#returning a book
def return_book(book_list): #Jose
    print("Return a book sucessfully called")

#adding a book
def add_book(): #Mahdi
    print("Add a book sucessfully called")

#removing a book
def remove_book(): #Jose
    print("Remove a book sucessfully called")

#displaying a list of books
def print_books(): #Mahdi
    print("Print books sucessfully called")

#saving the book catalog to a file
def save_books(book_list): #Jose
    print("Book catalog has been saved")
#main function for program
def main(): #Mahdi
    book_list =load_books()
    for b in book_list:
        print(b)
    selection = print_menu()
    while selection != 0:
        if selection == 1:
            search_input = input("Search for a book: ")
            search_books(search_input)
        elif selection == 2:
            borrow_book()
        elif selection == 3:
            return_book()
    if selection == 0:
        print("--Exit The System-- ")
        save_books()
        print("Good Bye!")
#calling main function to begin program        
if __name__ == "__main__":
    main()