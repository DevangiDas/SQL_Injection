import mysql.connector as msc

db = msc.connect(
  host="localhost",
  user="root",
  password="dba"
)

mycursor = db.cursor()


def createdb():
    mycursor.execute("SHOW DATABASES")
    result = mycursor.fetchall()
    print(type(result))
    print(result)
    dbase = input("Enter Database Name: ")
    db_exists = False
    t = list()
    for x in result:
        t.append(x[0])
    # print(t)
    # print(type(t))

    if any(dbase== x for x in t):
        imprint = "USE %s" % dbase
        mycursor.execute(imprint)
        print("using database as it already exits")
        db_exists = True
        
    if not db_exists:
        print("creating database")
        mycursor.execute(f"CREATE DATABASE {dbase}")
        imprint = "USE %s" % dbase
        mycursor.execute(imprint)

createdb()