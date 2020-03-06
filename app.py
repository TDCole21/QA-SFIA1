from flask import Flask, render_template
from data import dummydata
from flask_mysqldb import MySQL
from data import info
import os


app = Flask(__name__) #__name__ is for best practice

app.config["MYSQL_HOST"] = info.MySQLhost
app.config["MYSQL_USER"] = info.MySQLuser
app.config["MYSQL_PASSWORD"] = info.MySQLpassword
app.config["MYSQL_DB"] = info.MySQLdb


mysql = MySQL(app)

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template("index.html", name="Home")

@app.route('/actors')
def actors():
    cur = mysql.connection.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS testtable(ID INT(3) PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20));") #cur.execute requires SQL commands
    #cur.execute("INSERT INTO testtable (name) VALUES  (\"John Alley\");")
    cur.execute("SELECT * FROM Actors")
    mysql.connection.commit()
    rows = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()

    info = []

    for row in rows:
        info.append(row) #adding each row from the database into a newly created list, info    
    return render_template("actors.html", name="Actors", info1=info, posts=dummydata.dummyData)

@app.route('/films')
def films():
    cur = mysql.connection.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS testtable(ID INT(3) PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20));") #cur.execute requires SQL commands
    #cur.execute("INSERT INTO testtable (name) VALUES  (\"John Alley\");")
    cur.execute("SELECT * FROM Films")
    mysql.connection.commit() # This can go after the fetch all
    rows = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()

    info = []

    for row in rows:
        info.append(row) #adding each row from the database into a newly created list, info    
    return render_template("films.html", name="Films", info1=info)


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)