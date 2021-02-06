import sqlite3
import random, string

class Database:
    def __init__(self):
        pass
    
    def checkURL(self, url):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM enderecos WHERE url = '%s'" % url)
        return c.fetchone()[0] > 0

    def addURL(self, url, short=False):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        if(self.checkURL(url)):
            conn.close()
            return False
        
        if short:
            c.execute("SELECT COUNT(*) FROM enderecos WHERE short = '%s'" % short)
            count = c.fetchone()[0]
            if(count > 0):
                return {
                    'status': 'error',
                    'response': 'short already exists'
                }
        else:
            while True:
                short = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
                c.execute("SELECT COUNT(*) FROM enderecos WHERE short = '%s'" % short)
                count = c.fetchone()[0]
                if(count == 0):
                    break

        c.execute("INSERT INTO enderecos('url', 'short') VALUES ('%s', '%s')" % (url, short))
        conn.commit()

        c.execute("SELECT short FROM enderecos WHERE url='%s'" % url)
        return c.fetchone()[0]

    def getLink(self, url):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        if(self.checkURL(url)):
            c.execute("SELECT short FROM enderecos WHERE url LIKE '%s'" % url)
            
            result = c.fetchone()[0]
            conn.close()
            return result

        conn.close()
        return False

    def getUrl(self, short):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        
        c.execute("SELECT url FROM enderecos WHERE short = '%s'" % short)

        try:
            result = c.fetchone()[0]
            c.execute("""UPDATE enderecos
                        SET counter = counter + 1
                        WHERE short = '%s'
                        """ % short)
            conn.commit()
        except:
            result = ''

        conn.close()
        return result

    def getRank(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("""SELECT url, counter, short
                    FROM enderecos
                    ORDER BY counter DESC
                    LIMIT 5""")

        result = c.fetchall()

        return result

