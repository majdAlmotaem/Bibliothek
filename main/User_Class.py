#Klasse Benutzer erstellen
from Buch_Class import Buch
from Bibliothek_Class import Bibliothek

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

class User:
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname
        self.history = []

    # Methoden
    # Buch ausleihen 
    def ausleihen(title ,vorname, nachname):
        user_id = Bibliothek.find_user_id(vorname, nachname) #Id von User rausfinden 
        isbn = Buch.get_isbn_by_title(title) #ISBN von Buch rausfinden
        add_to_ausleihliste = 'INSERT INTO ausleihliste (User_id, ISBN, Ausgeliehen) VALUES (%s, %s, %s)' #Das Buch in ausleihliste hinzufügen
        if not Buch.Buch_status(isbn): # Verfügbarkeit und Buchstatus prüfen 
            print("Das Buch ist verfügbar und kann ausgeliehen werden.")
            print("Das Buch wurde erfolgreich ausgeliehen.")
            cursor.execute(add_to_ausleihliste, (user_id, isbn, 1))  # 1 für ausgeliehen
            connection.commit()
        else:
            print("Das Buch ist bereits ausgeliehen.")
            print("Versuchen Sie andere Bücher auszuleihen")

    # Buch Rückgabe
    def return_Buch(title):
        isbn = Buch.get_isbn_by_title(title)
        change_status = 'UPDATE ausleihliste SET ausgeliehen = 0 WHERE `ISBN` =%s' #Buch als nicht ausgeliehen speichern
        if Buch.Buch_status(isbn):
            print('Buch wird zurückgegeben')
            cursor.execute(change_status, (isbn))
            connection.commit()
        else:
            print("Ungültige Ausgabe!")

    # History anzeigen
    def history_anzeigen():
        pass