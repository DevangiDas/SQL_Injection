import mysql.connector as msc

db = msc.connect(
  host = "localhost",
  user = "root",
  password = "dba",
  database = "sqli"
)
print(db)
mycursor = db.cursor()

def login():
    username = input("Enter username: ")
    if(getpass(username)):
        return True

#function to display user               
# def display():
#     mycursor.execute("SELECT username,displayname FROM login_details")
#     res = mycursor.fetchall()
#     for x in res:
#         print("Username: ",x[0])
#         print("Display Name: ",x[1],"\n")

#function to delete user
def getpass(un):    #checks password for username
    password = input("Enter password: ")
    mycursor.execute("SELECT pass_word FROM login_details WHERE username = %s",(un,))
    #we need to convert 'un' to a tuple as that's how the records are stored/retrieved in sql
    res = mycursor.fetchone()
    # res = ('<value>',) so it is a tuple
    if (res==(password,)):
        return True

def delete():
    username = input("Enter username: ")
    if (getpass(username)):
        sql = "DELETE FROM login_details WHERE username = %s"
        mycursor.execute(sql,(username,))
        db.commit()
        print(mycursor.rowcount, "record(s) deleted")
    else:
        print("Please enter correct details")

if(login()):
    print("Login Successful")
    c = input("Do you want to delete your account? Y/N")
    if(c=='Y'):
        delete()