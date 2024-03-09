from Buch_Class import Buch
from Bibliothek_Class import Bibliothek
from UserHelper_Class import UserHelper
import datetime
#Verbindung mit SQL-Datenbank herstellen
from db_connection import *

current_date = datetime.date.today()

class User:
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname
        
    # Methoden
    # Buch ausleihen 
    def ausleihen(title: str ,vorname: str, nachname: str) -> str:
        return UserHelper.ausleihen(title, vorname, nachname)

    # Buch Rückgabe
    def return_Buch(title: str) -> str:
        return UserHelper.return_Buch(title)

    # History anzeigen
    def history_anzeigen(vorname: str, nachname: str) -> list:
        user_id = Bibliothek.find_user_id(vorname, nachname) #Id von User rausfinden 
        show_history = 'SELECT * FROM ausleihliste WHERE `User_Id`=%s'
        cursor.execute(show_history, (user_id))
        books = cursor.fetchall()
        if books:
            for book in books:
                print("-ISBN:",book['ISBN'], "-ausgeliehen von:", book['ausgeliehen_von'],"-ausgeliehen bis:", book['ausgeliehen_bis'])
        else:
            print("Sie haben keine Bücher in Ihre Liste")
            
