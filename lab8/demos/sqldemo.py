import sqlite3 as sqlite

# make connection
connection = sqlite.connect("new-db")   # if db doesn't exist... create it

# cursor is object created from connection
local_cursor = connection.cursor()    # .cursor() returns a cursor we can use

admin_query = "SELECT * FROM sqlite_master"
create_query = "CREATE TABLE dogs (" \
               "dog_id int NOT NULL," \
               "colour VARCHAR(20)," \
               "breed VARCHAR(30)," \
               "bark BOOLEAN," \
               "PRIMARY KEY(dog_id)" \
               ")"

insert_query = "INSERT INTO dogs VALUES (2, 'Tri Colour', 'Corgi', true)"
select_query = "SELECT * FROM dogs"


def run_query(query):
    data = local_cursor.execute(query)
    return data


# run_query(insert_query)
# sqlite only persists data if it's committed.
connection.commit()
print(run_query(select_query).fetchall())
