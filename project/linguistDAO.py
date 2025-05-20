import mysql.connector # to connect to the MySQL database
import dbconfig as cfg # importing the database credentials

# Defining the DAO for interaction with my freelance linguist database
class linguistDAO:
    # initialising class using credentials
    def __init__(self): 
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']
        self.connection = None
        self.cursor = None

    # function to connect to the database (will be used for all SQL queries)
    def getcursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    # function to close the cursor and database connection after each query
    def closeAll(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

# function to get all records from the linguists table
    def getAll(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM linguists"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"DEBUG: Retrieved rows from DB: {results}")
        returnArray = [self.convert_to_dict(row) for row in results]
        self.closeAll()
        print(f"DEBUG: Converted to dict: {returnArray}")
        return returnArray

# function to retrieve row by LinguistID
    def findByID(self, LinguistID):
        cursor = self.getcursor()
        sql = "SELECT * FROM linguists WHERE LinguistID = %s"
        cursor.execute(sql, (LinguistID,))
        result = cursor.fetchone()
        self.closeAll()
        return self.convert_to_dict(result) if result else None
    
# function which takes a dict object for linguist and inserts it to the database
    def create(self, linguist): 
        cursor = self.getcursor()
        sql = "INSERT INTO linguists (LinguistName, LinguistEmail, TargetLocale) VALUES (%s, %s, %s)" # not including LinguistID because this is set to autoincrement
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

# function to update a row of the table
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

# function to delete a row from the table
    def delete(self, LinguistID):
        cursor = self.getcursor()
        sql = "DELETE FROM linguists WHERE LinguistID = %s"
        cursor.execute(sql, (LinguistID,))
        self.connection.commit()
        self.closeAll()

# function to convert each row of results from a tuple into a dict  for use in flask
    def convert_to_dict(self, resultLine):
        keys = ['LinguistID', 'LinguistName', 'LinguistEmail', 'TargetLocale']
        return dict(zip(keys, resultLine))

# Create global instance of the class for use in Flask
dao = linguistDAO()
