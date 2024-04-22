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
        self.__genre = genre
     
        
    #Getters
    def get_isbn(self):
        return self.__isbn
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_genre_name(self):
        return Book.genre_name.get(self.__genre)
    
    def get_available(self):
        return self.__availability
    
    def get_availability(self):
        while self.__availability == True:
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
       self.__genre = genre_id
        
    def borrow_it(self):
        self.__availability = False
            
    def return_it(self):
        self.__availability = True
        
    def display(self):
        genre_name = self.get_genre_name()
        availability_bool = self.get_availability()
        print(f'ISBN: {self.__isbn}\nTitle: {self.__title}\nAuthor: {self.__author}\nGenre: {genre_name}\nAvailability: {availability_bool}')



    def print_all(books):
        print(f'{"ISBN":<16} {"Title":<30} {"Author":<21} {"Genre":<21} {"Availability":<11}')
        for book in books:
            book.display()
            
    def __str__(self):
        genre_name = self.get_genre_name()
        availability_bool = self.get_availability()
        results =  f"{self.__isbn:<14} {self.__title:<25} {self.__author:<25} {genre_name:<20} {availability_bool:<10}"

        return results
