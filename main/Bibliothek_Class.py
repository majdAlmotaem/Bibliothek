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
        self.vname = vorname
        self.nname = nachname

    #Benutzer Registieren
    def registieren(self, vorname, nachname):
        sql_query = 'INSERT INTO users (`Vorname`, `Nachname`) VALUES (%s, %s)'  #neue User in Datenbank hinzufügen
        cursor.execute(sql_query, (vorname,nachname))
        connection.commit()

    #get user id from database
    def find_user_id(vorname, nachname):
        find_user_query = 'SELECT User_Id FROM Users WHERE Vorname=%s AND Nachname=%s'
        cursor.execute(find_user_query, (vorname, nachname))
        result = cursor.fetchone()
        if result:
            return result['User_Id']
        else:
            return None

    #Funktion um zuprüfen, ob der User angemeldet ist. (bei Anmelden funktion) 
    def user_check(vname, nname):
        sql_query = 'SELECT * FROM users WHERE `Vorname`=%s AND `Nachname`=%s'
        cursor.execute(sql_query, (vname, nname))
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False