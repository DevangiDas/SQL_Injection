import mysql.connector as msc

db = msc.connect(
  host = "localhost",
  user = "root",
  password = "dba",
  database = "sqli"
)
print(db)
mycursor = db.cursor()

#function to create user
def isunique(un,x):
    if (un==x):
        return True

def insert(un):    
    nam = input("Enter name: ")
    pas = input("Save password: ")
    sql = "INSERT INTO login_details VALUES (%s, %s, %s)"
    val = (un, nam, pas)
    mycursor.execute(sql, val)
    db.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)
    print("Account created")

def checkuser():
    mycursor.execute("SELECT username FROM login_details")
    res = mycursor.fetchall()   # fetching list of already existing users
    username = input("Enter Unique username: ")
    if (res==[]):
        insert(username)
    else:
        t = list()
        for x in res:
            t.append(x[0])
        #print(t)
        if any(username==e for e in t):
            print("User already exists. Please choose another username.")
        else:
            insert(username)
checkuser()