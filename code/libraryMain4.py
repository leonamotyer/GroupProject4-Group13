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
    #Dicitonary holding library Id values as Keys, and their respective string as the values. 
    #Initialize empty book list and book counter, set counter to 0. 
    library_menu = {0:"Exit the system", 1: "Search for a book", 2: "Borrow a book", 3: "Return a book", 4: "Add a book", 5: "Remove a book", 6: "Print catalog"}
    book_list = []
    book_count = 0

  # loading a list of books from a file
    def load_books(self, book_list, csv_path): #Grace & Leona
        #check exsistence of file using os and exsist() with the csv_path that was defined in main> If file is not found ask again for valid file
        existence = os.path.exists(csv_path)
        while existence == False:
            csv_path = input("File not found. Re-enter book catalog filename: ")
            existence = os.path.exists(csv_path)
        else:
            #if file exsists, define as 'catalouge' and open in reading mode. Iterate through each line defining each varible as an individual item.
            catalouge = open(csv_path, 'r')
            for line in catalouge:
                items = line.rstrip('\n').split(',')
                isbn = items[0]
                title = items[1]
                author = items[2]
                genre = int(items[3])
                #check for availability, set default to true
                if items[4] == 'True':
                    availability = True
                else:
                    availability = False
                #append all books to the empty book list, and add to the counter 
                book_list.append(Book(isbn, title, author, genre, availability))
                self.book_count += 1 
        print('Book catalog has been loaded\n')
        catalouge.close()
        return catalouge

    #printing the options menu
    def print_menu(self, library_menu): #Leona
        print("Reader's Guild Library - Main menu\n")
        print('='*30)
        #using menu dicitonary to print options
        print(f"1. {library_menu.get(1)}")
        print(f"2. {library_menu.get(2)}")
        print(f"3. {library_menu.get(3)}")
        print(f"0. {library_menu.get(0)}\n")    
        selection = input("Enter your selection: ")
        #create if/else statement to test for the secret menu option, and a in-bedded if statment to test for invalid selections
        if selection == "2130":
            selection = self.secret_menu(library_menu)
        else:
            if selection not in ('0','1','2','3','2130'):
                print("Invalid option. Please try again.")
                return self.print_menu(library_menu)
        return int(selection)
    
    #seperate menu function for the secreat men.
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
        selection = input("Enter your selection: ")
        if selection not in ('0','1','2','3','4','5','6','2130'):#checking existance of selection in menu
            print("Invalid option. Please try again.")
            return self.secret_menu(library_menu)
        return int(selection)

    #searching for a book
    def search_books(self, book_list): #Grace
        #empty list for multiple search results, initilize as empty.
        search_result=[]
        print("-- Search for books --")
        search_input = input("Enter Search Value: ")
        for book_item in book_list:
            #define genre as its string name, compare user search input to each item in book list. should iterate and test against every variable
            genre= str(book_item.get_genre_name())
            #set the search_input to be accesseced in all lower case, as well as the compared variables
            if search_input.lower() in book_item.get_isbn().lower() \
                or search_input.lower() in book_item.get_title().lower() \
                or search_input.lower() in book_item.get_author().lower() \
                or search_input.lower() in genre.lower():
                #append found results to empty list
                search_result.append(book_item)
        #if no search results are found, user is sent back to menu
        if len(search_result) == 0:
            print("No matching books found.")
        else:
            #print all results found
            self.print_books(search_result)

    #borrowing a book
    def borrow_book(self): #Leona
        #ask for isbn from user, finds book using isbn
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
    def find_book_by_isbn(self, isbn): #Grace & Leona
        for book_item in self.book_list: #iterating through book list to find book by isbn
            if book_item.get_isbn() == isbn: #checking if isbn exists in class
                return book_item        #returning found item
        return None #returning none if not found
    
    #returning a book
    def return_book(self): #Leona
        print("Return a book sucessfully called")
        #Ask user for isbn, determine book by value
        isbn = input("Enter a book ISBN to return in formatt 999-9999999999: ")
        book = self.find_book_by_isbn(isbn)
        #if book is in list, check availabilty. If is not available, call the return_it function, else let the user know it is not borrowed
        #iterate throug book_list to see if book with the isbn exsists
        if book is not None:
            if not book.get_available():
                book.return_it()
                print(book.get_title(), "with ISBN:",isbn,"has been returned")
            else:
                print(book.get_title(), "with ISBN:",isbn," is not currently borrowed")
        else:
            print("Book not found with that ISBN")
            
    #adding a book
    def add_book(self): #Grace
        print("-- Add a book --")
        # input ISBN, title, author, and genre name
        isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
        title = input("Enter title: ")
        author = input("Enter author name: ")
        idGenre_name = input("Enter the genre: ").lower()
        #iterate through list of genre names, if the genre does not match, ask user to re-input
        if idGenre_name not in ('romance', 'mystery', 'science fiction', 'thriller', 'young adult', "childrens fiction", 'self-help','self help', 'fantasy', 'historical fiction', 'poetry'):
            print("Invalid genre. Choices are: Romance, Mystery, Science Fiction, Thriller, " +
                    "Young Adult, Children's Fiction, Self-help, Fantasy, Historical Fiction, Poetry")
            idGenre_name = input("Enter the genre: ")
        #set genre_name to respective id number 
        else:
            if idGenre_name == 'romance':
                idGenre_name = 0
            elif idGenre_name == 'mystery':
                idGenre_name = 1
            elif idGenre_name == 'science fiction':
                idGenre_name= 2
            elif idGenre_name == 'thriller':
                idGenre_name = 3
            elif idGenre_name == 'young adult':
                idGenre_name = 4
            elif idGenre_name == "childrens fiction":
                idGenre_name= 5
            elif idGenre_name == 'self-help':
                idGenre_name = 6
            elif idGenre_name == 'self help':
                idGenre_name = 6
            elif idGenre_name == 'fantasy':
                idGenre_name = 7
            elif idGenre_name == 'historical fiction':
                idGenre_name = 8
            elif idGenre_name == 'poetry':
                idGenre_name = 9
        
        # call find_book_by_isbn to check if the book already exsits, if not, appened to booklist alongside all new information  
        while self.find_book_by_isbn(isbn) == -1:
            print("A book with that ISBN already exists.")
            isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
        # add book to book_list
        else:
            self.book_list.append(Book(isbn, title, author, idGenre_name, True))
            print(f"'{title}' with ISBN {isbn} successfully added.\n")
    
    #removing a book
    def remove_book(self, book_list): #Grace
        remove_isbn = input("Enter a book ISBN to remove: ")
        found_book = self.find_book_by_isbn(remove_isbn)
        if found_book is not None:
            isbn= remove_isbn
            title= found_book.get_title()
            book_list.remove(found_book)
            print(f"{title} with ISBN {isbn} successfully removed")
        else:
            print("No book found with that ISBN")

    #displaying a list of books
    def print_books(self, book_list:list): #Grace
        print('-- Print book catalog --')
        # Iterates through the list of books and prints the information for each book.
        print(f'{"ISBN":<14} {"Title":<25} {"Author":<25} {"Genre":<20} {"Availability":<20}')
        print(f"{14*'-'} {25*'-'} {25*'-'} {20*'-'} {20*'-'}")
        for book_item in book_list:
            genre= str(book_item.get_genre_name())
            print(f"{book_item.get_isbn():<14} {book_item.get_title():<25} {book_item.get_author():<25} {genre:<20} {book_item.get_availability():<20}")
        
#saving the book catalog to a file
    def save_books(self, book_list, csv_path): #Leona 
        for book in book_list:
            catalouge = open(csv_path, 'a')
            catalouge.write(f'{book.get_isbn()}, {book.get_title()}, {book.get_author()}, {book.get_genre()}, {book.get_available()}\n')
        print("Book catalog has been saved")
        catalouge.close()
    #main function for program


def main(): #Leona
  # set up a list of books
    print("Starting the system ...")
    #prompt the user to enter the filename of the CSV file containing the book catalog.
    csv_path = input("Enter book catalog filename: ")
    #initialize instance of the Library_Catalouge class and load the books from the CSV file.
    libraryCatalouge= Library_Catalouge()
    libraryCatalouge.load_books(Library_Catalouge.book_list, csv_path)
    # present the menu
    selection = libraryCatalouge.print_menu(libraryCatalouge.library_menu)
    
    #You present menu to the user and continue executing the selected functionality until the user chooses to exit (selection == 0).
    while selection != 0:      
        if selection == 2130:
            selection = libraryCatalouge.secret_menu(libraryCatalouge.library_menu)  
        if selection == 1:
            libraryCatalouge.search_books(libraryCatalouge.book_list)
        elif selection == 2:
            libraryCatalouge.borrow_book()
        elif selection == 3:
            libraryCatalouge.return_book()
        elif selection == 4:
            libraryCatalouge.add_book()
            selection = libraryCatalouge.secret_menu(libraryCatalouge.library_menu)
        elif selection == 5:
            libraryCatalouge.remove_book(libraryCatalouge.book_list)
            selection = libraryCatalouge.secret_menu(libraryCatalouge.library_menu)
        elif selection == 6:
            libraryCatalouge.print_books(libraryCatalouge.book_list)
            selection = libraryCatalouge.secret_menu(libraryCatalouge.library_menu)

        #When the user chooses to exit, you save the updated book list to the CSV file and print a goodbye message.
        elif selection == 0:
            print("--Exit The System-- ")
            libraryCatalouge.save_books(Library_Catalouge.book_list, csv_path)
            print("Good Bye!")
          
    save_path = "./saved_books.csv"
    libraryCatalouge.save_books(Library_Catalouge.book_list, save_path)
#calling main function to begin program        
if __name__ == "__main__":
    main()
