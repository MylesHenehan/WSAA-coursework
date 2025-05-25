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

# function to get all records from the linguists table along with their rates from the rates table
    def getAll(self):
        cursor = self.getcursor()
        sql = """
            SELECT 
                l.LinguistID,
                l.LinguistName, 
                l.LinguistEmail, 
                l.TargetLocale, 
                r.PerWordRate, 
                r.HourlyRate
            FROM linguists AS l
            LEFT JOIN rates AS r ON l.LinguistID = r.LinguistID
            ORDER BY l.LinguistID
        """
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"DEBUG: Retrieved rows from DB: {results}")
        returnArray = [self.convert_to_dict(row) for row in results]
        self.closeAll()
        print(f"DEBUG: Converted to dict: {returnArray}")
        return returnArray

# function to retrieve linguist info (including rates) by ID
    def findLinguistWithRate(self, LinguistID):
        cursor = self.getcursor()
        sql = """
            SELECT l.LinguistID, l.LinguistName, l.LinguistEmail, l.TargetLocale,
                r.PerWordRate, r.HourlyRate
            FROM linguists l
            LEFT JOIN rates r ON l.LinguistID = r.LinguistID
            WHERE l.LinguistID = %s
        """
        cursor.execute(sql, (LinguistID,))
        result = cursor.fetchone()
        self.closeAll()

        if result:
            return {
                "LinguistID": result[0],
                "LinguistName": result[1],
                "LinguistEmail": result[2],
                "TargetLocale": result[3],
                "PerWordRate": result[4],
                "HourlyRate": result[5]
            }
        else:
            return None
    
# function which takes a dict object for linguist and inserts it to the database
    def create(self, linguist): 
        cursor = self.getcursor()
        # Insert into linguists table
        sql = "INSERT INTO linguists (LinguistName, LinguistEmail, TargetLocale) VALUES (%s, %s, %s)"
        values = (
            linguist.get("LinguistName"),
            linguist.get("LinguistEmail"),
            linguist.get("TargetLocale")
        )
        cursor.execute(sql, values)
        linguist_id = cursor.lastrowid

        # Insert into rates table if rates are provided
        if "PerWordRate" in linguist or "HourlyRate" in linguist:
            sql_rate = """
                INSERT INTO rates (LinguistID, PerWordRate, HourlyRate) VALUES (%s, %s, %s)
            """
            cursor.execute(sql_rate, (
                linguist_id,
                linguist.get("PerWordRate"),
                linguist.get("HourlyRate")
            ))

        self.connection.commit()
        self.closeAll()

        return self.findLinguistWithRate(linguist_id)

# function to update a row of the table
    def update(self, LinguistID, linguist):
        cursor = self.getcursor()
        sql1 = "UPDATE linguists SET LinguistName=%s, LinguistEmail=%s, TargetLocale=%s WHERE LinguistID = %s"
        values1 = (
            linguist.get("LinguistName"),
            linguist.get("LinguistEmail"),
            linguist.get("TargetLocale"),
            LinguistID
        )
        cursor.execute(sql1, values1)

        sql2 = "UPDATE rates SET PerWordRate=%s, HourlyRate=%s WHERE LinguistID = %s"
        values2 = (
            linguist.get("PerWordRate"),
            linguist.get("HourlyRate"),
            LinguistID
        )
        cursor.execute(sql2, values2)
        self.connection.commit()
        self.closeAll()


# function to delete a row from the table
    def delete(self, LinguistID):
        cursor = self.getcursor()
        sql = "DELETE FROM linguists WHERE LinguistID = %s"
        cursor.execute(sql, (LinguistID,))
        self.connection.commit()
        self.closeAll()

# function to convert each row of results from a tuple into a dict for use in flask
    def convert_to_dict(self, resultLine):
        keys = ['LinguistID', 'LinguistName', 'LinguistEmail', 'TargetLocale', 'PerWordRate', 'HourlyRate']
        return dict(zip(keys, resultLine))

# Create global instance of the class for use in Flask
dao = linguistDAO()