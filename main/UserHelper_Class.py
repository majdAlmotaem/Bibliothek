from Buch_Class import Buch
from Bibliothek_Class import Bibliothek
import datetime
#Verbindung mit SQL-Datenbank herstellen
from db_connection import *

current_date = datetime.date.today()

class UserHelper:

    @staticmethod
    def ausleihen(title: str ,vorname: str, nachname: str) -> str:
        user_id = Bibliothek.find_user_id(vorname, nachname) #Id von User rausfinden 
        isbn = Buch.get_isbn_by_title(title) #ISBN von Buch rausfinden
        add_to_ausleihliste = 'INSERT INTO ausleihliste (User_id, ISBN, ausgeliehen_von) VALUES (%s, %s, %s)' #Das Buch in ausleihliste hinzufügen
        change_status = 'UPDATE Books SET ausgeliehen = 1 WHERE `ISBN` = %s'
        if isbn:
            if not Buch.buch_status(isbn): # Verfügbarkeit und Buchstatus prüfen 
                print("Das Buch ist verfügbar und kann ausgeliehen werden.")
                print("Das Buch wurde erfolgreich ausgeliehen.")
                cursor.execute(add_to_ausleihliste, (user_id, isbn, current_date))  # das Buch wird in tabelle ausgeliehen hinzugefügt
                cursor.execute(change_status, (isbn))
                connection.commit()
            else:
                print("Das Buch ist bereits ausgeliehen.")
                print("Versuchen Sie andere Bücher auszuleihen")
        else:
            print("Das Buch ist leider nicht Verfügbar")

    
    @staticmethod
    # Buch Rückgabe
    def return_Buch(title: str) -> str:
        isbn = Buch.get_isbn_by_title(title)
        change_status = 'UPDATE Books SET ausgeliehen = 0 WHERE `ISBN` =%s' #Buch als nicht ausgeliehen speichern
        abgabe_datum = 'UPDATE ausleihliste SET ausgeliehen_bis = %s WHERE `ISBN` = %s' # Abgabedatum setzen
        if isbn: 
            if Buch.buch_status(isbn):
                print('Buch wird zurückgegeben')
                cursor.execute(change_status, (isbn))
                cursor.execute(abgabe_datum, (current_date, isbn))
                connection.commit()
            else:
                print("Das Buch ist nicht als ausgeliehen gespeichert")
        else:
            print("Das Buch ist leider nicht Verfügbar")
