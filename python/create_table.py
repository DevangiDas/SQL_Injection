import mysql.connector as msc

db = msc.connect(
  host = "localhost",      #
  user = "root",
  password = "dba",
  database = "sqli"
)
print(db)
mycursor = db.cursor() 

def create():
    
    mycursor.execute('''CREATE TABLE IF NOT EXISTS login_details (
                    username VARCHAR(25) PRIMARY KEY,
                    displayname VARCHAR(25) NOT NULL,
                    pass_word VARCHAR(25) NOT NULL)''')
    db.commit()
    print("Ok,",mycursor.lastrowid,"records retrieved")

def display():
    mycursor.execute("DESC login_details")
    res = mycursor.fetchall()
    for x in res:
        print(x)

create()
display()