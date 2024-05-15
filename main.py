import csv
import sqlite3

con = sqlite3.connect('WBbase10.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS Client(
    id integer primary key autoincrement,
    f text,
    i text,
    o text
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Postavshik(
    id integer primary key autoincrement,
    Number integer,
    f text,
    i text,
    o text
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Tovar(
    id integer primary key autoincrement,
    Name text,
    count integer
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Rabotnik(
    id integer primary key autoincrement,
    f text,
    i text,
    o text
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Postavki(
    id integer primary key autoincrement,
    datetime text,
    idPostavshik integer references Postavshik(id),
    idTovar integer references Tovar(id),
    count integer,
    idRabotnik integer references Rabotnik(id)
    )
    ''')

with open('Postavki.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['id'] and row['datetime'] and row['idPostavshik'] and row['idTovar'] and row['count'] and row['idRabotnik']:
            cur.execute("INSERT INTO Postavki(id,datetime,idPostavshik, idTovar, count,idRabotnik) VALUES (?,?,?,?,?,?)", (row['id'],
                                                                                                                       row['datetime'],
                                                                                                                       row['idPostavshik'],
                                                                                                                       row['idTovar'],
                                                                                                                       row['count'],
                                                                                                                       row['idRabotnik'],
                                                                                                                       ))

con.commit()
con.close()
