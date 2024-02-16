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

#Menü
if user_auswahl == "1": #als Gast fortfahren kann nur die Büchliste angezeigt 
    print("-"*20)
    print("Als Gast dürfen Sie nur unsere Bücherliste angucken.\nUm Bücher auszuleihen, müssen Sie Sich bitte registieren!")
    Buch.show_books()
 #Bei Anmeldung soll der User sein Name eingeben, damit geprüft wird, ob der angemeldet ist.
elif user_auswahl == "2":
    anmelden_vorname = (input("Vorname: "))
    anmelden_nachname = (input("Nachname: "))
    user_check= Bibliothek.user_check(anmelden_vorname, anmelden_nachname)
    print("-"*20)
    if user_check == False:
        print("User wurde nicht gefunden")
        exit
    else:
        print("Hallo", anmelden_vorname) 
        print("Wie kann ich Ihnen weiter helfen?\n1. Buch ausleihen\n2. Buch zurückgeben\n3. Historie anzeigen")
        print("-"*20)
        option_Auswahl = input("wählen Sie ein Option aus\n")
        if option_Auswahl == "1": #Buchausleihen
            Buch.show_books() 
            title_eingabe = input("Geben Sie Title des Buch ein..")
            print("-"*20)
            User.ausleihen(title_eingabe, anmelden_vorname, anmelden_nachname)
        elif option_Auswahl == "2": #Buchzurückgeben
            title_eingabe = input("Geben Sie Title des Buch ein..")
            print("-"*20)
            User.return_Buch(title_eingabe)
        elif option_Auswahl == "3": #Historie anzeigen
            User.history_anzeigen
        else:
            print("Ungültige Eingabe!")
elif user_auswahl == "3": #Registieren
    print("-"* 20)
    print("Bitte Daten eingeben")
    add_vorname = Bibliothek(input("Vorname: "))
    add_nachname = Bibliothek(input("Nachname: "))
    Bibliothek.registieren(add_vorname,add_nachname)
else:
    print("Ungültige Eingabe!")