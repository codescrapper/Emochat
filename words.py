import sqlite3

conn = sqlite3.connect('emochat.db')

def makeTable():
    c = conn.cursor()
    c.execute('create table words (word varchar(100))')

def addWord(word):
    c = conn.cursor()
    c.execute("select * from words where word like '%"+word+"%'")
    if not c.fetchone():
        c.execute("insert into words values ('"+word+"')")
        print word + ' added in list'
    else:
        print word + ' already present in list'
    c.commit()
    c.close()
