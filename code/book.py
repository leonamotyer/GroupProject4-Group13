class Book:
        #genre info displayed in a dict, keys as genre ID, and values as name of genre
    __genre_info__= {
        0:"Romance",
        1:"Mystery",
        2:"Science Fiction",
        3:"Thriller",
        4:"Young Adult",
        5:"Children's Fiction",
        6:"Self-help",
        7:"Fantasy",
        8:"Historical Fiction",
        9:"Poetry"
    }
    def __init__(self, isbn, title, author, genre, availability):
        self.title = title
        self.author = author
        self.availability = availability
        self.isbn = isbn
        self.genre = genre
     
        
    #Getters
    def get_isbn(self):
        return self.isbn
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_genre_name(self):
        return self.genre
    
    def get_availability(self):
        if self.availability == True:
            return "Available"
        else:
            return "Borrowed"
        
    #setters
    def set_isbn(self, isbn):
        self.isbn = isbn
        
    def set_title(self, title):
        self.title = title
        
    def set_author(self, author):
        self.author = author
    
    def set_genre(self, genre):
        self.genre = genre
        
    def borrow_it(self):
        self.availability = "Borrowed"
            
    def return_it(self):
        self.availability = "Available"
        
    def display(self):
        print(f'ISBN: {self.isbn}\nTitle: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nAvailability: {self.availability}')
    
    
    def print_all(self, catalogue):
        print(f'{"ISBN":<16} {"Title":<30} {"Author":<21} {"Genre":<21} {"Availability":<11}')
        for book in catalogue:
            print(f'{book.get_isbn():<15} {book.get_title():<30} {book.get_author():<20} {book.get_genre():<20} {book.get_availability():<10}')
            
    def __str__(self):
        results =  f"{self.isbn:<15} {self.title:<30} {self.author:<20} {self.genre:<20} {self.availability:<10}"
   
        return results