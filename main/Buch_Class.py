from BuchHelper_Class import BuchHelper
#Verbindung mit SQL-Datenbank herstellen
from db_connection import *

#klasse Buch erstellen
class Buch: #Bauplan 
    def __init__(self, isbn, title, autor, genre): #Konstruktor
        self.title = title
        self.isbn = isbn
        self.autor = autor
        self.genre = genre

    
    def get_isbn_by_title(title: str) -> str:
        return BuchHelper.get_isbn_by_title(title)

    #diese Methode prüft, ob das Buch bei uns existiert.
    def buch_check(isbn: str) -> bool:
        return BuchHelper.buch_check(isbn)

    #diese Methode prüft den Status des Buch, ob das ausgeliehen ist.
    def buch_status(isbn: str) -> bool:
        return BuchHelper.buch_status(isbn)
        
    #Bücher anzeigen
    def show_books() -> list:
        return BuchHelper.show_books()

    #Buch nach kategorie suchen
    def search_book_by_genre(genre: str) -> str:
        pass


