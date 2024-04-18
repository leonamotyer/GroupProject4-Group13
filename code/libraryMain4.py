from book import Book

def load_books():
    pass

def print_menu():
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

def search_books():
    print("Search for a book")

def borrow_book():
    print("Borrow a book")

def find_book_by_isbn():
    pass

def return_book():
    print("Return a book")

def add_book():
    pass

def remove_book():
    pass

def print_books():
    pass

def save_books():
    print("Book catalog has been saved")

def main():
    selection = print_menu()
    while selection != 0:
        if selection == 1:
            search_books()
        elif selection == 2:
            borrow_book()
        elif selection == 3:
            return_book()
    if selection == 0:
        print("--Exit The System-- ")
        save_books()
        print("Good Bye!")
if __name__ == "__main__":
    main()