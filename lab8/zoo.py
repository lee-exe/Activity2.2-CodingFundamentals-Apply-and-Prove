import sqlite3 as sqlite

connection = sqlite.connect("test-db")
cursor = connection.cursor()

sql_file = open("fish.sql")
preset_record = open("preset-record.sql")


def run_query(query):
    sql_string = query.read()
    cursor.executescript(sql_string)


print(cursor.execute("SELECT * FROM fish").fetchall().sort())
connection.commit()



