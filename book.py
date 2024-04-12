class Book:

    
    def __init__(self, isbn, title, author, genre, availability):
        self.title = title
        self.author = author
        self.availability = availability
        self.isbn = isbn
        self.genre = genre
     
        
    #Getters
    def getisbn(self):
        return self.isbn
    
    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author
    
    def getGenre(self):
        return self.genre
    
    def getLocation(self):
        return self.availability
    #setters
    def setisbn(self, isbn):
        self.isbn = isbn
        
    def setTitle(self, title):
        self.title = title
        
    def setAuthor(self, author):
        self.author = author
    
    def setGenre(self, genre):
        self.genre = genre
        
    def setLocation(self, location):
        self.availability = location
        
    def display(self):
        print(f'ISBN: {self.isbn}\nTitle: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nAvailability: {self.availability}')
    
    
    def printAll(self, catalogue):
        print(f'{"ISBN":<15} {"Title":<30} {"Author":<20} {"Genre":<20} {"Availability":<10}')
        for book in catalogue:
            print(f'{book.isbn:<15} {book.title:<30} {book.author:<20} {book.genre:<20} {book.availability:<10}')
