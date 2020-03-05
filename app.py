from flask import Flask, render_template
from templates import dummydata
from flask_mysqldb import MySQL


app = Flask(__name__) #__name__ is for best practice

app.config["MYSQL_HOST"] = '34.65.134.225'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = 'Rosliston21'
app.config["MYSQL_DB"] = 'accountdb'

mysql = MySQL(app)

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    cur = mysql.connection.cursor()
    cur.execute("CREATE TABLE testtable(ID INT(3), name VARCHAR(20));")
    mysql.connection.commit()
    cur.close()


    return render_template("index.html", name="Home", page="active", posts=dummydata.dummyData)

@app.route('/actors')
def actors():
    return render_template("actors.html", name="Actors", page="active", posts=dummydata.dummyData)

@app.route('/films')
def films():
    return render_template("films.html", name="Films", page="active", posts=dummydata.dummyData)


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)