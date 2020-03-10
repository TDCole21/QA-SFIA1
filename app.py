from flask import Flask, render_template, request, redirect, url_for
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

######################################################################################################################################################################
############################################################################     HOME     ############################################################################
######################################################################################################################################################################

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template("index.html", name="Home")

######################################################################################################################################################################
###########################################################################     ACTORS     ###########################################################################
######################################################################################################################################################################

@app.route('/actors', methods=['GET', 'POST']) # Read Function
def actors():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Actors")
    mysql.connection.commit()
    rows = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()

    info = []

    for row in rows:
        info.append(row) #adding each row from the database into a newly created list, info  

    return render_template("actors.html", name="Actors", info1=info)

@app.route('/actors/create', methods=['GET', 'POST']) # Create function
def actors_create():
    if request.method == "POST":
        details=request.form
        name=details['name']
        if name != "":
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Actors (Name) VALUES (%s)", [name])
            mysql.connection.commit()
            cur.close()

    return redirect(url_for('actors'))


@app.route('/actors/delete', methods=['GET', 'POST']) # Delete function
def actors_delete():
    if request.method == "POST":
        details=request.form
        name=details['name']
        if name != "":
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM Actors WHERE Actor_Name = (%s)", [name])
            mysql.connection.commit()
            cur.close()

    return redirect(url_for('actors'))

# Add an if statement that means you can only delete soemthing from within the database
 

@app.route('/actors/update', methods=['GET', 'POST']) # Update function
def actors_update():
    if request.method == "POST":
        details=request.form
        fromname=details['initialname']
        toname=details['finalname']
        if fromname != "" and toname != "":
            cur = mysql.connection.cursor()
            cur.execute("UPDATE Actors SET Actor_Name=(%s) WHERE Actor_Name=(%s)", [toname, fromname])
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('actors'))

    return redirect(url_for('actors'))

#######################################################################################################################################################################
############################################################################     FILMS     ############################################################################
#######################################################################################################################################################################


@app.route('/films', methods=['GET', 'POST']) # Read Function
def films():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Films")
    mysql.connection.commit()
    rows = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()

    info = []

    for row in rows:
        info.append(row) #adding each row from the database into a newly created list, info  

    return render_template("films.html", name="Films", info1=info)

@app.route('/films/create', methods=['GET', 'POST']) # Create function
def films_create():
    if request.method == "POST":
        details=request.form
        name=details['name']
        if name != "":
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Films (Film_Name) VALUES (%s)", [name])
            mysql.connection.commit()
            cur.close()

    return redirect(url_for('films'))


@app.route('/films/delete', methods=['GET', 'POST']) # Delete function
def films_delete():
    if request.method == "POST":
        details=request.form
        films=details['films']
        cur=mysql.connection.cursor()
        cur.execute("DELETE FROM Films WHERE Film_Name = (%s)", [films]) #works in GCP SQL
        mysql.connection.commit()
        cur.close()
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM Films")
    mysql.connection.commit()
    rows = cur.fetchall()
    cur.close()
    
    return redirect(url_for('films'))
 

@app.route('/films/update', methods=['GET', 'POST']) # Update function
def films_update():
    if request.method == "POST":
        details=request.form
        fromname=details['initialname']
        toname=details['finalname']
        if fromname != "" and toname != "":
            cur = mysql.connection.cursor()
            cur.execute("UPDATE Films SET Film_Name=(%s) WHERE Film_Name=(%s)", [toname, fromname])
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('films'))

    return redirect(url_for('films'))

#######################################################################################################################################################################
############################################################################     MISC.     ############################################################################
#######################################################################################################################################################################

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)