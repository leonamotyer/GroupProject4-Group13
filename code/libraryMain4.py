'''
 library app class
'''
import os
import csv
import book


class LibraryApp:
    '''
    comprised of various functions, including a main() entry function to control overall processing. 
    The functions listed below are required but you may use additional functions too.
    '''

    def load_books(self, book_list, file_path):
        '''
        loading books from a CSV file
        @param book_list - list - a list of book objects
        @param file_path - string - the pathname to the CSV file
        @return line_count - int - the number of books loaded
        '''
        # Receives an empty list and pathname to an existing CSV file
        # check the file existence
        existence = os.path.exists(file_path)
        while not existence:
            file_path = input("File not found. Re-enter book catalog filename: ")
            existence = os.path.exists(file_path)
        # Opens the file for reading with the specified encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            line_count = 0
            for line in reader:
                isbn = line[0]
                title = line[1]
                author = line[2]
                genre = int(line[3])
                if line[4] == 'True':
                    available = True
                else:
                    available = False
                book_list.append(
                    book.Book(isbn, title, author, genre, available))
                line_count += 1
        # Closes the file
        file.close()
        print("Book catalog has been loaded.\n")
        # Returns the number of books loaded
        return line_count


    def print_menu(self, menu_heading, menu_options):
        '''
        print_menu
        @param menu_heading - string - the heading for the menu
        @param menu_options - dictionary - the menu options
        @return selection - string - the user's selection
        @return check_list - list - menu item check record
        '''
        # receiving menu options(dictionary) and menu heading(string)
        # displaying menu heading
        heading_prefix = "Reader's Guild Library"
        heading = heading_prefix + " - " + menu_heading[0]
        print(heading)
        print(len(heading)*"=")
        count = 0
        check_list = []
        last_line = ""
        # displaying menu options
        for key, value in menu_options.items():
            check_list.append(key)
            count += 1
            if count==4:
                last_line = key + ". " + value
                if menu_heading[0] == 'Main Menu':
                    break
                continue
            print(f'{key}. {value}')
        print(last_line)
        # receiving user input
        selection = input("Enter your selection: ")
        while menu_heading[0] == 'Main Menu' and len(selection) > 1:
            if selection == '2130':
                menu_heading[0] = "Librarian Menu"
                print("")
                selection,check_list = self.print_menu(menu_heading,menu_options)
            else:
                print("Invalid option.")
                selection = input("Enter your selection: ")
        # check if user input is in menu options
        while selection not in check_list:
            print("Invalid option.")
            selection = input("Enter your selection: ")
        # returning user input
        return selection, check_list


    def search_books(self, book_list):
        '''
        search_books
        @param book_list - list - a list of book objects
        '''
        print("-- Search for books --")
        # Iterates through the list of books and checks if the search string appears in
        # isbn, title, author, or genre name. If any match is found, the book is added to the search result list.
        search_str = input("Enter search value: ")
        search_result = []
        for b in book_list:
            if search_str.lower() in b.get_isbn().lower() \
                or search_str.lower() in b.get_title().lower() \
                or search_str.lower() in b.get_author().lower() \
                or search_str.lower() in b.get_genre_name().lower():
                search_result.append(b)
        if len(search_result) == 0:
            print("No matching books found.")
        else:
            self.print_books(search_result)
        print("")


    def borrow_book(self, book_list: list):
        '''
        borrow_book
        '''
        print("-- Borrow a book --")
        # input isbn
        isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
        index = self.find_book_by_isbn(book_list, isbn)
        # index is -1 if book is not found
        if index == -1:
            print("No book found with that ISBN.")
        else:
            # check if book is available
            if book_list[index].get_available():
                # borrow book
                book_list[index].borrow_it()
                print(f"'{book_list[index].get_title()}' with {book_list[index].get_isbn()} " + 
                      "successfully borrowed.")
            else:
                print(f"'{book_list[index].get_title()}' with {book_list[index].get_isbn()} " +
                    "is not currently available.")
        print("")


    def find_book_by_isbn(self, book_list, isbn):
        '''
        find_book_by_isbn
        @param book_list - list - a list of book objects
        @param isbn - string - the ISBN of the book to find
        @return index - int - the index of the book in the list
        '''
        # Iterates through the list of books and checks if the ISBN matches the search ISBN.
        # If a match is found, the index of the book is returned.
        for b in book_list:
            if b.get_isbn() == isbn:
                return book_list.index(b)
        return -1

    def return_book(self, book_list: list):
        '''
        return_book
        @param book_list - list - a list of book objects
        '''
        print("-- Return a book --")
        # input isbn
        isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
        index = self.find_book_by_isbn(book_list, isbn)
        if index != -1:
            if not book_list[index].get_available():
                book_list[index].return_it()
                print(f"'{book_list[index].get_title()}' with {book_list[index].get_isbn()} " +
                      "successfully returned.")
            else:
                print(f"'{book_list[index].get_title()}' with {book_list[index].get_isbn()} " +
                      "is not currently borrowed.")
        else:
            print("No book found with that ISBN.")
        print("")

    def add_book(self, book_list: list):
        '''
        add_book
        @param book_list - list - a list of book objects
        '''
        print("-- Add a book --")
        # input ISBN, title, author, and genre name
        isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
        title = input("Enter title: ")
        author = input("Enter author name: ")
        genre_name = input("Enter the genre: ")
        # check if genre is valid, interate book.Book.GENRE_NAME_DICT to match if the value matches the genre name
        genre_num = book.Book.REV_GENRE_NAME_DICT.get(genre_name, '-1')
        while genre_num == '-1':
            print("Invalid genre. Choices are: Romance, Mystery, Science Fiction, Thriller, " +
                  "Young Adult, Children's Fiction, Self-help, Fantasy, Historical Fiction, Poetry")
            genre_name = input("Enter the genre: ")
            genre_num = book.Book.REV_GENRE_NAME_DICT.get(genre_name, '-1')
        # check if ISBN already exists
        while self.find_book_by_isbn(book_list, isbn) != -1:
            print("A book with that ISBN already exists.")
            isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
        # add book to book_list
        book_list.append(book.Book(isbn, title, author, genre_num, True))
        print(f"'{title}' with ISBN {isbn} successfully added.\n")


    def remove_book(self, book_list:list):
        '''
        remove_book
        @param book_list - list - a list of book objects
        '''
        print("-- Remove a book --")
        # input ISBN
        isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
        index = self.find_book_by_isbn(book_list, isbn)
        if index != -1:
            title = book_list[index].get_title()
            del book_list[index]
            print(f"'{title}' with ISBN {isbn} successfully removed.")
        else:
            print("No book found with that ISBN.")
        print("")


    def print_books(self, book_list:list):
        '''
        print_books
        @param book_list - list - a list of book objects
        '''
        print('-- Print book catalog --')
        # Iterates through the list of books and prints the information for each book.
        print(f'{"ISBN":<14} {"Title":<25} {"Author":<25} {"Genre":<20} {"Availability":<20}')
        print(f"{14*'-'} {25*'-'} {25*'-'} {20*'-'} {20*'-'}")
        for b in book_list:
            print(f"{b.get_isbn():<14} {b.get_title():<25} {b.get_author():<25} {b.get_genre_name():<20} {b.get_availability():<20}")
        print("")

    def save_books(self, book_list, path_name):
        '''
        save_books
        @param book_list - list - a list of book objects
        @param path_name - string - the pathname to the CSV file
        '''
        # Receives a list of book objects and a pathname to a CSV file
        # Opens the file for writing with the specified encoding
        with open(path_name, 'w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',')
            # Iterates through the list of books and writes the information for each book to the file.
            for b in book_list:
                writer.writerow([b.get_isbn(), b.get_title(), b.get_author(), b.get_genre(), b.get_availability()])
        # Closes the file
        file.close()



MENU_OPTIONS = {"1":"Search for books","2":"Borrow a book","3":"Return a book",
                "0":"Exit the system","4":"Add a book", "5":"Remove a book",
                "6":"Print catalog"}
# main method
def main():
    '''
    main
    '''
    # set up a list of books
    book_list = []
    menu_heading = ["Main Menu"]
    library_app = LibraryApp()
    print("Starting the system ...")
    csv_path = input("Enter book catalog filename: ")
    library_app.load_books(book_list, csv_path)
    # present the menu
    loop = True
    while loop:
        # options according to user choice
        selection,_ = library_app.print_menu(menu_heading,MENU_OPTIONS)
        print("")
        # decide by selection
        if selection == '1':
            library_app.search_books(book_list)
        if selection == '2':
            library_app.borrow_book(book_list)
        if selection == '3':
            library_app.return_book(book_list)
        if selection == '4':
            library_app.add_book(book_list)
        if selection == '5':
            library_app.remove_book(book_list)
        if selection == '6':
            library_app.print_books(book_list)
        if selection == '0':
            print("-- Exit the system --")
            print("Book catalog has been saved.")
            print("Good Bye!")
            loop = False
    # save books to the designated path
    save_path = "./saved_books.csv"
    library_app.save_books(book_list,save_path)


if __name__ == "__main__":
    main()
