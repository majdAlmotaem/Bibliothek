#klassen importieren
from Bibliothek_Class import Bibliothek
from Buch_Class import Buch
from User_Class import User

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
            
        
#Begrüßung 
print("------ Willkommen in unserer Bibliothek ------")

#Frage ob der User angemeldet ist 
print("1. Als Gast fortfahren\n2. Anmelden\n3. Regstieren")
user_auswahl = input('')

#User Check
if user_auswahl == "1": #als Gast fortfahren kann nur die Büchliste angezeigt 
    print("-----------------------")
    print("Als Gast dürfen Sie nur unsere Bücherliste angucken.\nUm Bücher auszuleihen, müssen Sie Sich bitte registieren!")
    Buch.show_books()
elif user_auswahl == "2": #Bei Anmeldung soll der User sein Name eingeben, damit geprüft wird, ob der angemeldet ist.
    add_vorname = str(input("Vorname: "))
    add_nachname = str(input("Nachname: "))
    user_check= Bibliothek.user_check(add_vorname, add_nachname)
    print("-----------------------")
    if user_check == False:
        print("User wurde nicht gefunden")
        exit
    else: 
        print("Wie kann ich Ihnen weiter helfen?\n1. Buch ausleihen\n2. Buch zurückgeben\n3. Historie anzeigen")
        print("-----------------------")
        option_Auswahl = input("wählen Sie ein Option aus\n")
        if option_Auswahl == "1": #Buchausleihen
            Buch.show_books() 
            title_eingabe = input("Geben Sie Title des Buch ein..")
            print("-----------------------")
            User.ausleihen(title_eingabe, add_vorname, add_nachname)
        elif option_Auswahl == "2": #Buchzurückgeben
            title_eingabe = input("Geben Sie Title des Buch ein..")
            print("-----------------------")
            User.return_Buch(title_eingabe)
        elif option_Auswahl == "3": #Historie anzeigen
            User.history_anzeigen
        else:
            print("Ungültige Eingabe!")
elif user_auswahl == "3": #Registieren
    Bibliothek.registieren()
else:
    print("Ungültige Eingabe!")