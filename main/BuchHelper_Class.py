#Verbindung mit SQL-Datenbank herstellen
from db_connection import *


class BuchHelper:
    # Die statische Methode wird aufgerufen, ohne eine Instanz der Klasse zu erstellen
    @staticmethod
    def get_isbn_by_title(title: str) -> str:
        get_isbn_query = 'SELECT ISBN FROM books WHERE Title = %s'
        cursor.execute(get_isbn_query, (title,))
        result = cursor.fetchone()
        if result:
            return result['ISBN']
        else:
            return None

    @staticmethod
    def buch_check(isbn: str) -> bool:
        book_status_check = 'SELECT * FROM books WHERE `ISBN`=%s'
        cursor.execute(book_status_check, (isbn,))
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False

    @staticmethod
    def buch_status(isbn: str) -> bool:
        if BuchHelper.buch_check(isbn):
            buch_status_check = 'SELECT * FROM books WHERE `ISBN`=%s AND `ausgeliehen`="1"'
            cursor.execute(buch_status_check, (isbn,))
            result = cursor.fetchone()
            if result:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def show_books() -> list:
        sql_query = 'SELECT * FROM Books'
        num = 1 #zähler für die Bücherliste
        print("-"*20)
        print("Hier ist unsere Bücherliste:")
        cursor.execute(sql_query)
        books = cursor.fetchall()
        for book in books:
            print(num,"-ISBN:", book['ISBN'], "-Title:", book['Title'],"-Autor:", book['Autor'],"-Genre:", book['Genre'],)
            num += 1
