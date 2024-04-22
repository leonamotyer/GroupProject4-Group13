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
    
    book_list = []
    book_count = 0

  # loading a list of books from a file
    def load_books(self, book_list, csv_path): #Grace
        existence = os.path.exists(csv_path)
        catalouge = open(csv_path, 'r')
        while existence == False:
            csv_path = input("File not found. Re-enter book catalog filename: ")
            existence = os.path.exists(csv_path)
        else:
            for line in catalouge:
                items = line.rstrip('\n').split(',')
                isbn = items[0]
                title = items[1]
                author = items[2]
                genre = int(items[3])
                if items[4] == 'True':
                    availability = True
                else:
                    availability = False
                book_list.append(Book(isbn, title, author, genre, availability))
                self.book_count += 1 
        print('Book catalog has been loaded\n')
        

    #printing the options menu
    def print_menu(self, library_menu): #Leona
        print("Reader's Guild Library - Main menu\n")
        print('='*30)
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
        book = Library_Catalouge.find_book_by_isbn(borrow_isbn)
        if book is not None:
            if book.get_available==True:
                print("Book has been borrowed")
                Book.borrow_it()
            else:
                print("Book is not available")
        else:
            print("Book not found")

    #finding a book by ISBN
    def find_book_by_isbn(self, isbn): #Grace
        for book_item in self.book_list:
            if book_item.get_isbn() == isbn:
                return self.book_list.index(book_item)
            else:
                return ('-1')

    #returning a book
    def return_book(book_list): #Jose
        print("Return a book sucessfully called")
        return_isbn = input("Enter a book ISBN to return: ")
        found_book = self.find_book_by_isbn(book_list, return_isbn)
        if found_book is not None:
            if not found_book.get_available:
                found_book.return_it()
                print("Book has been returned")
            else:
                print("this book was not borrowed")
        else:
            print("Book not found")

    #adding a book
    def add_book(self): #Mahdi
        print("-- Add a book --")
        # input ISBN, title, author, and genre name
        isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
        title = input("Enter title: ")
        author = input("Enter author name: ")
        idGenre_name = input("Enter the genre: ")
        idGenre_num= Book.genre_name.get(idGenre_name, '-1')
        while idGenre_num == '-1':
            print("Invalid genre. Choices are: Romance, Mystery, Science Fiction, Thriller, " +
                    "Young Adult, Children's Fiction, Self-help, Fantasy, Historical Fiction, Poetry")
            idGenre_name = input("Enter the genre: ")
            idGenre_num = Book.genre_name.get(idGenre_name, '-1')
        
        while self.find_book_by_isbn(isbn) != -1:
            print("A book with that ISBN already exists.")
            isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
        # add book to book_list
        self.book_list.append(Book(isbn, title, author, idGenre_num, True))
        print(f"'{title}' with ISBN {isbn} successfully added.\n")
  
    #removing a book
    def remove_book(self, book_list): #Jose
        remove_isbn = input("Enter a book ISBN to remove: ")
        found_book = self.find_book_by_isbn(book_list, remove_isbn)
        if found_book is not None:
            book_list.remove(found_book)
        else: 
            print("Book not found")
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
    def save_books(self, book_list, file_path): #Jose
     with open(file_path,'books', newline='', encoding='utf-8') as file:
        writer = csv.writer(books)
        for book in book_list:
            writer.writerow([book.get_isbn(), book.get_title(), book.get_author(), book.get_genre(), book.get_available()])
        print("Book catalog has been saved")
    #main function for program


def main(): #Mahdi
    library_menu = {0:"Exit the system", 1: "Search for a book", 2: "Borrow a book", 3: "Return a book"}
  # set up a list of books
    print("Starting the system ...")
    csv_path = input("Enter book catalog filename: ")
    libraryCatalouge= Library_Catalouge()
    libraryCatalouge.load_books(Library_Catalouge.book_list, csv_path)
    # present the menu
    loop= True
    while loop:
        selection = libraryCatalouge.print_menu(library_menu)
        if selection == 1:
            libraryCatalouge.search_books(libraryCatalouge.book_list)
        elif selection == 2:
            libraryCatalouge.borrow_book(libraryCatalouge.book_list)
        elif selection == 3:
            libraryCatalouge.return_book(libraryCatalouge.book_list)
        elif selection == 0:
            print("--Exit The System-- ")
            libraryCatalouge.save_books()
            print("Good Bye!")
        
    save_path = "./saved_books.csv"
    libraryCatalouge.save_books(book_list,save_path)
#calling main function to begin program        
if __name__ == "__main__":
    main()