import create_table
import mysql.connector as msc
from flask import Flask, request, render_template
app = Flask(__name__, static_folder='css',
            template_folder='frontend')  # Flask constructor


# create table if not exists
create_table.createtable()

# db connection
db = msc.connect(
    host="localhost",
    user="root",
    password="dba",
    database="sqli"
)
print(db)
mycursor = db.cursor()


def check_user(username, password):  # checks password and username
    mycursor.execute("SELECT username,pass_word FROM login_details WHERE username = '%s' AND pass_word = '%s'" % (
        username, password))
    res = mycursor.fetchall()
    if (res):
        return True


@app.route('/', methods=['POST'])
def getvalue():
    username = request.form['username']
    password = request.form['password']
    if (check_user(username, password)):
        return render_template('login_success.html', u=username, p=password)
    return render_template('login_fail.html')


@app.route('/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
