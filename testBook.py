from book import Book

def main():
    catalogue = []
    bookOne = Book(isbn = '978-0441172719', title = 'Dune', author = 'Frank Herbert', genre = 'Science Fiction', availability = 'Borrowed')
    catalogue.append(bookOne) 
    print(bookOne.display())

    searchInput = input('Search Books: ')
    bookTwo = Book(isbn = '978-0375822742', title = 'City of Ember', author = 'Jeanne DuPrau', genre = 'Young Adult', availability = 'Available')
    catalogue.append(bookTwo) 
    print(search(catalogue, searchInput))
    
    bookThree = Book(isbn = '978-0394800165', title = 'Green Eggs and Ham', author = 'Dr. Seuss', genre = 'Childrens Fiction', availability = 'Available')
    catalogue.append(bookThree) 
    print(bookThree.print_all(Book.catalogue))

def search(catalogue, searchInput):#needs more work
    if searchInput in catalogue:
        return f'Found a match... Title: {self.title}, Isbn: {self.isbn}'
    else:
        return 'No match found'


if __name__ == '__main__':
    main()