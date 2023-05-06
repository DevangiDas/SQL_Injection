import create_table
import mysql.connector as msc
from flask import Flask, render_template, request
app = Flask(__name__, static_folder='css',
            template_folder='frontend')  # Flask constructor


# create table if not exists
create_table.createtable()

db = msc.connect(
    host="localhost",
    user="root",
    password="dba",
    database="sqli"
)
print(db)
mycursor = db.cursor()

# function to create user


def insert(un, nam, pas):
    sql = "INSERT INTO login_details VALUES (%s, %s, %s)"
    val = (un, nam, pas)
    mycursor.execute(sql, val)
    db.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)
    print("Account created")


def check_unique_user(username, displayname, password):
    mycursor.execute("SELECT username FROM login_details")
    res = mycursor.fetchall()   # fetching list of already existing users
    if (res == []):  # base case (when there are no users)
        insert(username, displayname, password)
        return True
    else:
        t = list()
        for x in res:
            t.append(x[0])
        if any(username == e for e in t):
            return False
        else:
            insert(username, displayname, password)
            return True


@app.route('/', methods=['POST'])
def getvalue():
    username = request.form['username']
    displayname = request.form['displayname']
    password = request.form['password']
    if (check_unique_user(username, displayname, password)):
        return render_template('signup_success.html', u=username, d=displayname, p=password)
    else:
        msg = "User already exists. Please choose another username."
    return render_template('signup_fail.html', msg=msg)


@app.route('/')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
