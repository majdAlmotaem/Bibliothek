from abc import ABC, abstractmethod

class Manager(ABC):

    @abstractmethod
    def add_book(self, title):
        pass

    @abstractmethod
    def remove_book(self, title):
        pass


class BibliothekManager(Manager):
    
    def add_book(self, title):
        pass

    def remove_book(self, title):
        pass
