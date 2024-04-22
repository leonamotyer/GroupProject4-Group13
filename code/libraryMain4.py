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
    library_menu = {0:"Exit the system", 1: "Search for a book", 2: "Borrow a book", 3: "Return a book", 4: "Add a book", 5: "Remove a book", 6: "Print catalog"}
    book_list = []
    book_count = 0

  # loading a list of books from a file
    def load_books(self, book_list, csv_path): #Grace
        existence = os.path.exists(csv_path)
        while existence == False:
            csv_path = input("File not found. Re-enter book catalog filename: ")
            existence = os.path.exists(csv_path)
        else:
            catalouge = open(csv_path, 'r')
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
        catalouge.close()
        return catalouge

    #printing the options menu
    def print_menu(self, library_menu): #Leona
        print("Reader's Guild Library - Main menu\n")
        print('='*30)
        print(f"1. {library_menu.get(1)}")
        print(f"2. {library_menu.get(2)}")
        print(f"3. {library_menu.get(3)}")
        print(f"0. {library_menu.get(0)}\n")    
        selection = input("Enter your selection: ")
        if selection == 2130:
            selection = self.secret_menu(library_menu)
        else:
            if selection not in ('0','1','2','3',):
                print("Invalid option. Please try again.")
                return self.print_menu(library_menu)
        return int(selection)
    
    def secret_menu(self, library_menu): #Leona
        print("Reader's Guild Library - Secret menu\n")
        print('='*30)
        print(f"1. {library_menu.get(1)}")
        print(f"2. {library_menu.get(2)}")
        print(f"3. {library_menu.get(3)}")
        print(f"4. {library_menu.get(4)}")
        print(f"5. {library_menu.get(5)}")
        print(f"6. {library_menu.get(6)}")
        print(f"0. {library_menu.get(0)}\n")    
        selection = int(input("Enter your selection: "))
        if selection not in library_menu.keys(): #checking existance of selection in menu
            print("Invalid option. Please try again.")
            self.secret_menu()
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
    def borrow_book(self): #Leona
        #should work but need to be tested once find book is programmed 
        isbn = input("Enter a book ISBN in formatt 999-9999999999: ")
        book = self.find_book_by_isbn(isbn)
        if book is not None: #checking if book exists
            if book.get_available(): #checking if book is available
                print(book.get_title(), "with ISBN:",isbn, "has been borrowed")
                book.borrow_it()
            else: #book is not available
                print(book.get_title(), "with ISBN:",isbn," is not available")
        else: #book does not exist
            print("No book found with that ISBN.")
            
    #finding a book by ISBN
    def find_book_by_isbn(self, isbn): #Grace
        for book_item in self.book_list: #iterating through book list to find book by isbn
            if book_item.get_isbn() == isbn: #checking if isbn exists in class
                return book_item        #returning found item
        return None #returning none if not found
    
    #returning a book
    def return_book(self): #Jose
        print("Return a book sucessfully called")
        isbn = input("Enter a book ISBN to return in formatt 999-9999999999: ")
        book = self.find_book_by_isbn(isbn)
        if book is not None:
            if not book.get_available():
                book.return_it()
                print(book.get_title(), "with ISBN:",isbn,"has been returned")
            else:
                print(book.get_title(), "with ISBN:",isbn," is not currently borrowed")
        else:
            print("Book not found with that ISBN")
            
    #adding a book
    def add_book(self): #Mahdi
        print("-- Add a book --")
        # input ISBN, title, author, and genre name
        isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
        title = input("Enter title: ")
        author = input("Enter author name: ")
        idGenre_name = input("Enter the genre: ")
        idGenre_num= Book.GENRE_NAME.get(idGenre_name, '-1')
        while idGenre_num == '-1':
            print("Invalid genre. Choices are: Romance, Mystery, Science Fiction, Thriller, " +
                    "Young Adult, Children's Fiction, Self-help, Fantasy, Historical Fiction, Poetry")
            idGenre_name = input("Enter the genre: ")
            idGenre_num = Book.GENRE_NAME.get(idGenre_name, '-1')
        
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
    def save_books(self, book_list, csv_path): #Jose
        catalouge = open(csv_path, 'w') 
        for book in book_list:
            catalouge.write(f'{book.get_isbn()}, {book.get_title()}, {book.get_author()}, {book.get_genre()}, {book.get_available()}\n')
        print("Book catalog has been saved")
    #main function for program


def main(): #Mahdi
  # set up a list of books
    print("Starting the system ...")
    csv_path = input("Enter book catalog filename: ")
    libraryCatalouge= Library_Catalouge()
    libraryCatalouge.load_books(Library_Catalouge.book_list, csv_path)
    # present the menu
    loop= True
    while loop:
        selection = libraryCatalouge.print_menu(libraryCatalouge.library_menu)
        if selection == 1:
            libraryCatalouge.search_books(libraryCatalouge.book_list)
        elif selection == 2:
            libraryCatalouge.borrow_book()
        elif selection == 3:
            libraryCatalouge.return_book()
        elif selection == 4:
            libraryCatalouge.add_book()
        elif selection == 5:
            libraryCatalouge.remove_book()
        elif selection == 6:
            libraryCatalouge.print_books()
        elif selection == 0:
            print("--Exit The System-- ")
            libraryCatalouge.save_books(Library_Catalouge.book_list, csv_path)
            print("Good Bye!")
            loop = False
        
    save_path = "./saved_books.csv"
    libraryCatalouge.save_books(Library_Catalouge.book_list, save_path)
#calling main function to begin program        
if __name__ == "__main__":
    main()