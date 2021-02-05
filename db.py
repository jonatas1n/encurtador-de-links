import sqlite3
import base64

# conn = sqlite3.connect('database.db')
# c = conn.cursor()

class Database:
    def __init__(self):
        pass
    
    def checkURL(self, url):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM enderecos WHERE url = '%s'" % url)
        return c.fetchone()[0] > 0

    def addURL(self, url):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        if(self.checkURL(url)):
            print('Essa URL já existe')
            conn.close()
            return False
        
        c.execute("INSERT INTO enderecos('url') VALUES ('%s')" % url)
        c.execute("SELECT id, url FROM enderecos WHERE url='%s'" % url)
        conn.commit()
        conn.close()
        return c.fetchone()

    def getLink(self, url):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        if(self.checkURL(url)):
            c.execute("SELECT id FROM enderecos WHERE url LIKE '%s'" % url)
            conn.commit()
            result = c.fetchone()[0]
            print(result)
            return result

        conn.close()
        return False

    def closeConn(self):
        conn.close()