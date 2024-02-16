
#Verbindung mit SQL-Datenbank herstellen
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='Bibliothek',
    charset= 'utf8mb4',
    cursorclass= pymysql.cursors.DictCursor
)
cursor = connection.cursor() 

#klasse Buch erstellen
class Buch: #Bauplan 
    def __init__(self, isbn,title, autor, genre): #Konstruktor
        self.title = title
        self.isbn = isbn
        self.autor = autor
        self.genre = genre

    #funktion to get isbn 
    def get_isbn_by_title(title):
        get_isbn_query = 'SELECT ISBN FROM books WHERE Title = %s'
        cursor.execute(get_isbn_query, (title,))
        result = cursor.fetchone()
        if result:
            return result['ISBN']
        else:
            return None

    #Verfügbarkeitprüfen von Buch
    def Buch_check(isbn):
        book_status_check = 'SELECT * FROM books WHERE `ISBN`=%s' #wird geprüft ob das Buch in unsere Bibliothek existiert 
        cursor.execute(book_status_check, (isbn))
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False
        
    #Buchstatus checken
    def Buch_status(isbn):
        if Buch.Buch_check(isbn):
            # Wenn das Buch existiert, prüfe den Buchstatus, ob das ausgeliehen ist
            buch_status_check = 'SELECT * FROM books WHERE `ISBN`=%s AND `ausgeliehen`="1"'
            cursor.execute(buch_status_check, (isbn))
            result = cursor.fetchone()
            if result:
                print("ok")
                return True
            else:
                return False
        else:
            return False
        
    #Bücher anzeigen
    def show_books():
        sql_query = 'SELECT * FROM Books'
        num = 1 #zähler für die Bücherliste
        print("-"*20)
        print("Hier ist unsere Bücherliste:")
        cursor.execute(sql_query)
        books = cursor.fetchall()
        for book in books:
            print(num,"-ISBN:", book['ISBN'], "-Title:", book['Title'],"-Autor:", book['Autor'],"-Genre:", book['Genre'],)
            num += 1