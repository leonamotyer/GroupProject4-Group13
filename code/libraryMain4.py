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
    selection = input("Enter your selection: ")
    if selection not in library_menu.keys():
        print("Invalid option. Please try again.")
        print_menu()
    return selection

def search_books():
    pass

def borrow_book():
    pass

def find_book_by_isbn():
    pass

def return_book():
    pass

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
    print_menu()
    if selection == 0:
        print("--Exit The System-- ")
        save_books()
        print("Good Bye!")
        exit()

if __name__ == "__main__":
    main()