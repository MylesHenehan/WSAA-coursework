import mysql.connector
import dbconfig as cfg

class linguistDAO:
    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']
        self.connection = None
        self.cursor = None

    def getcursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def getAll(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM linguists"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = [self.convertToDictionary(row) for row in results]
        self.closeAll()
        return returnArray

    def findByID(self, LinguistID):
        cursor = self.getcursor()
        sql = "SELECT * FROM linguists WHERE LinguistID = %s"
        cursor.execute(sql, (LinguistID,))
        result = cursor.fetchone()
        self.closeAll()
        return self.convertToDictionary(result) if result else None

    def create(self, linguist):
        cursor = self.getcursor()
        sql = "INSERT INTO linguists (LinguistName, LinguistEmail, TargetLocale) VALUES (%s, %s, %s)"
        values = (
            linguist.get("LinguistName"),
            linguist.get("LinguistEmail"),
            linguist.get("TargetLocale")
        )
        cursor.execute(sql, values)
        self.connection.commit()
        linguist["LinguistID"] = cursor.lastrowid
        self.closeAll()
        return linguist

    def update(self, LinguistID, linguist):
        cursor = self.getcursor()
        sql = "UPDATE linguists SET LinguistName=%s, LinguistEmail=%s, TargetLocale=%s WHERE LinguistID = %s"
        values = (
            linguist.get("LinguistName"),
            linguist.get("LinguistEmail"),
            linguist.get("TargetLocale"),
            LinguistID
        )
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, LinguistID):
        cursor = self.getcursor()
        sql = "DELETE FROM linguists WHERE LinguistID = %s"
        cursor.execute(sql, (LinguistID,))
        self.connection.commit()
        self.closeAll()

    def convertToDictionary(self, resultLine):
        keys = ['LinguistID', 'LinguistName', 'LinguistEmail', 'TargetLocale']
        return dict(zip(keys, resultLine))

# Create instance
linguistDAO = linguistDAO()
