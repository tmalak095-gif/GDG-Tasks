from abc import ABC, abstractmethod

# Part 1 – Abstract Base Class: LibraryItem
class LibraryItem(ABC):
    def __init__(self, item_id, title, author):
        self.item_id = item_id
        self.title = title
        self.author = author

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    def is_available(self):
        return True

# Part 2 – Subclasses with Encapsulation
class Book(LibraryItem):
    def __init__(self, item_id, title, author, num_pages):
        super().__init__(item_id, title, author)
        self.__num_pages = num_pages
        self.__available = True

    def get_pages(self):
        return self.__num_pages

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.__num_pages}"

    def get_type(self):
        return 'Physical Book'

class EBook(LibraryItem):
    def __init__(self, item_id, title, author, file_size_mb):
        super().__init__(item_id, title, author)
        self.__file_size_mb = file_size_mb
        self.__available = True

    def get_file_size(self):
        return self.__file_size_mb

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Size: {self.__file_size_mb}MB"

    def get_type(self):
        return 'eBook'
