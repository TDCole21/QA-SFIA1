from flask import Flask, render_template
from data import dummydata
from flask_mysqldb import MySQL
from data import info


app = Flask(__name__) #__name__ is for best practice

app.config["MYSQL_HOST"] = info.MYSQL_HOST
app.config["MYSQL_USER"] = info.MYSQL_USER
app.config["MYSQL_PASSWORD"] = info.MYSQL_PASSWORD
app.config["MYSQL_DB"] = info.MYSQL_DB

mysql = MySQL(app)

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    cur = mysql.connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS testtable(ID INT(3) PRIMARY KEY, name VARCHAR(20));") #cur.execute requires SQL commands
    cur.execute("SELECT * FROM testtable")
    mysql.connection.commit()
    rows = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()

    info = []

    for row in rows:
        info.append(row) #adding each row from the database into a newly created list, info

    return render_template("index.html", name="Home", page="active", info1=info, posts=dummydata.dummyData)

@app.route('/actors')
def actors():
    return render_template("actors.html", name="Actors", page="active", posts=dummydata.dummyData)

@app.route('/films')
def films():
    return render_template("films.html", name="Films", page="active", posts=dummydata.dummyData)


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)