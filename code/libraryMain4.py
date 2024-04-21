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
import os
import csv
class Library_Catalouge():

  # loading a list of books from a file
  def load_books(self, book_list, catalouge): #Grace
      existence = os.path.exists(catalouge)
      while not existence:
          catalouge = input("File not found. Re-enter book catalog filename: ")
          existence = os.path.exists(catalouge)
      with open(catalouge, 'r', encoding='utf-8') as catalouge:
          catalouge_reader = csv.reader(catalouge, delimiter=',')
          book_count = 0
          for line in catalouge_reader:
              isbn = line[0]
              title = line[1]
              author = line[2]
              genre = int(line[3])
              if line[4] == 'True':
                  availability = True
              else:
                  availability = False
              book_list.append(Book(isbn, title, author, genre, availability))
              book_count += 1 
          return book_count

    #printing the options menu
    def print_menu(self, library_menu): #Leona
        print("Welcome to the Library\n")
        print(f"1. {library_menu.get(1)}")
        print(f"2. {library_menu.get(2)}")
        print(f"3. {library_menu.get(3)}")
        print(f"0. {library_menu.get(0)}\n")    
        selection = int(input("Enter your selection: "))
        if selection not in library_menu.keys():
            print("Invalid option. Please try again.")
            self.print_menu()
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
        else:
            return ('-1')

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
    def print_books(self, book_list:list): #Mahdi
        print('-- Print book catalog --')
        # Iterates through the list of books and prints the information for each book.
        print(f'{"ISBN":<14} {"Title":<25} {"Author":<25} {"Genre":<20} {"Availability":<20}')
        print(f"{14*'-'} {25*'-'} {25*'-'} {20*'-'} {20*'-'}")
        for book_item in book_list:
            genre= str(book_item.get_genre_name())
            print(f"{book_item.get_isbn():<14} {book_item.get_title():<25} {book_item.get_author():<25} {genre:<20} {book_item.get_availability():<20}")
    #saving the book catalog to a file
    def save_books(): #Jose
        print("Book catalog has been saved")
    #main function for program


def main(): #Mahdi
  library_menu = {0:"Exit the system", 1: "Search for a book", 2: "Borrow a book", 3: "Return a book"}
        # set up a list of books
    book_list = load_books()
    print("Starting the system ...")
    csv_path = input("Enter book catalog filename: ")
    libraryCatalouge= Library_Catalouge()
    libraryCatalouge.load_books(book_list, csv_path)
    # present the menu
    loop= True
    while loop:
        selection = libraryCatalouge.print_menu(library_menu)
        if selection == 1:
            libraryCatalouge.search_books(book_list)
        elif selection == 2:
            libraryCatalouge.borrow_book(book_list)
        elif selection == 3:
            libraryCatalouge.return_book()
        elif selection == 0:
            print("--Exit The System-- ")
            libraryCatalouge.save_books()
            print("Good Bye!")
        
    save_path = "./saved_books.csv"
#calling main function to begin program        
if __name__ == "__main__":
    main()
