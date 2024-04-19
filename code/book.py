class Book:
        #genre info displayed in a dict, keys as genre ID, and values as name of genre
    genre_name= {
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
        self.__title = title
        self.__author = author
        self.__availability = availability
        self.__isbn = isbn
        self.__genre = Book.genre_name.get(genre)
     
        
    #Getters
    def get_isbn(self):
        return self.__isbn
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_genre_name(self):
        return Book.genre_name.get(self.__genre)
    
    def get_availability(self):
        if self.__availability == True:
            return "Available"
        else:
            return "Borrowed"
        
    #setters
    def set_isbn(self, isbn):
        self.__isbn = isbn
        
    def set_title(self, title):
        self.__title = title
        
    def set_author(self, author):
        self.__author = author
    
    def set_genre(self, genre_id):
       self.__genre = Book.genre_name.get(genre_id)
        
        
    def borrow_it(self):
        self.__availability = "Borrowed"
            
    def return_it(self):
        self.__availability = "Available"
        
    def display(self):
        print(f'ISBN: {self.__isbn}\nTitle: {self.__title}\nAuthor: {self.__author}\nGenre: {self.__genre}\nAvailability: {self.__availability}')
    
    
    def print_all(self,catalogue):
        print(f'{"ISBN":<16} {"Title":<30} {"Author":<21} {"Genre":<21} {"Availability":<11}')
        for book in catalogue:
            print(f'{book.get_isbn():<15} {book.get_title():<30} {book.get_author():<20} {book.get_genre():<20} {book.get_availability():<10}')
            
    def __str__(self):
        results =  f"{self.__isbn:<14} {self.__title:<25} {self.__author:<25} {self.__genre:<20} {self.__availability:<10}"
   
        return results