class Book:
    def __init__(self, isbn, title, author, genre, availability):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__availability = availability

    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_genre_name(self):
        genre_list = ["Romance", "Mystery", "Science Fiction", "Thriller", "Young Adult", "Children’s Fiction", "Self-help", "Fantasy", "Historical Fiction", "Poetry"]
        return genre_list[self.__genre]

    def get_availability(self):
        return self.__availability

    def borrow_it(self):
        self.__availability = False

    def return_it(self):
        self.__availability = True

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_genre(self, genre):
        self.__genre = genre

    def __str__(self):
        return "{:14s} {:25s} {:25s} {:20s} {:s}".format(self.__isbn, self.__title,
            self.__author, self.get_genre_name(), str(self.__availability))
    
