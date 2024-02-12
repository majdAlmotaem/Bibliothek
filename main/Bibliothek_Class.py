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

#klasse Bibliothek
class Bibliothek:
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname

    #Benutzer Registieren
    def registieren():
        print("----------------------")
        print("Bitte Daten eingeben")
        add_vorname = str(input("Vorname: "))
        add_nachname = str(input("Nachname: "))
        #sql query schreiben und neue User in Datenbank hinzufügen
        sql_query = 'INSERT INTO users (`Vorname`, `Nachname`) VALUES (%s, %s)'
        cursor.execute(sql_query, (add_vorname,add_nachname))
        connection.commit()

    def find_user_id(vorname, nachname):
        find_user_query = 'SELECT User_Id FROM Users WHERE Vorname=%s AND Nachname=%s'
        cursor.execute(find_user_query, (vorname, nachname))
        result = cursor.fetchone()
        if result:
            return result['User_Id']
        else:
            return None

    #Funktion um zuprüfen, ob der User angemeldet ist.
    def user_check(vorname, nachname):
        sql_query = 'SELECT * FROM users WHERE `Vorname`=%s AND `Nachname`=%s'
        cursor.execute(sql_query, (vorname, nachname))
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False