from flask import Flask, request, render_template
app = Flask(__name__, static_folder='css', template_folder='frontend') #flask constructor

import mysql.connector as msc

db = msc.connect(
  host = "localhost",
  user = "root",
  password = "dba",
  database = "sqli"
)
print(db)
mycursor = db.cursor()

def check_user(username, password):
    if(getpass(username, password)):
        return True

def getpass(un, pwd):    #checks password for username
    mycursor.execute("SELECT pass_word FROM login_details WHERE username = %s",(un,))
    #we need to convert 'un' to a tuple as that's how the records are stored/retrieved in sql
    res = mycursor.fetchone()
    # res = ('<value>',) so it is a tuple
    if (res==(pwd,)):
        return True

@app.route('/', methods=['POST'])
def getvalue():
    username = request.form['username']
    password = request.form['password']
    if(check_user(username,password)):
        return render_template('login_success.html', u=username, p=password)
    return render_template('login_fail.html')

@app.route('/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
   app.run(debug=True)