from flask import Flask, render_template, request, redirect, url_for
from data import dummydata
from flask_mysqldb import MySQL
from data import info
import os
import re


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
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Actors")
    mysql.connection.commit()
    actornames = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.execute("SELECT * FROM Films")
    mysql.connection.commit()
    filmnames = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()

    actorselection = []
    filmselection = []

    for row in actornames:
        actorselection.append(row) #adding each row from the database into a newly created list, info  
    
    for row in filmnames:
        filmselection.append(row) #adding each row from the database into a newly created list, info 

    return render_template("index.html", name="Home", actorselection=actorselection, filmselection=filmselection)


@app.route('/home/search', methods=['GET', 'POST']) # Delete function
def actor_film_search():
    if request.method == "POST":
        details=request.form
        films=details['filmname']
        actors=details['actorname']
        
        cur = mysql.connection.cursor()
        cur.execute("select Actor_Name from Actors where Actor_ID in (select ActorID from Film_Actor where FilmID=(SELECT Film_ID from Films WHERE Film_Name=(%s)))", [films])
        mysql.connection.commit()
        selectactornames = cur.fetchall() #built in function to return a tuple, list or dictionary
        cur.execute("select Film_Name from Films where Film_ID in (select FilmID from Film_Actor where ActorID=(SELECT Actor_ID from Actors WHERE Actor_Name=(%s)))", [actors])
        mysql.connection.commit()
        selectfilmnames = cur.fetchall() 
        cur.execute("SELECT * FROM Films")
        mysql.connection.commit()
        filmnames = cur.fetchall() #built in function to return a tuple, list or dictionary
        cur.execute("SELECT * FROM Actors")
        mysql.connection.commit()
        actornames = cur.fetchall() #built in function to return a tuple, list or dictionary
        cur.close()

        actorchoice = []
        filmchoice = []
        actorselection = []
        filmselection = []

        for row in selectactornames:
            actorchoice.append(row) #adding each row from the database into a newly created list, info  
                    
        for row in actornames:
            actorselection.append(row) #adding each row from the database into a newly created list, info
        
        for row in filmnames:
            filmselection.append(row) #adding each row from the database into a newly created list, info  

        for row in selectfilmnames:
            filmchoice.append(row) #adding each row from the database into a newly created list, info 
    
    if len(selectactornames)==0 and films != "- Choose a Film -":
        actorchoice=[["There are no actors that star in this film"]] 
    
    if len(selectfilmnames)==0 and actors != "- Choose an Actor -":
        filmchoice=[["This actor does not star in any films"]] 

    if films == "- Choose a Film -" and actors == "- Choose an Actor -":
        return redirect(url_for('home'))
    
    elif films != "- Choose a Film -" and actors == "- Choose an Actor -":
        return render_template("index.html", name="Home", film="Actors starring in "+films+":", actorchoice=actorchoice, filmchoice=filmchoice, actorselection=actorselection, filmselection=filmselection)

    elif films == "- Choose a Film -" and actors != "- Choose an Actor -":
        return render_template("index.html", name="Home", actor="Films starring "+actors+":", actorchoice=actorchoice, filmchoice=filmchoice, actorselection=actorselection, filmselection=filmselection)


    return render_template("index.html", name="Home",actor="Films starring "+actors+":", film="Actors starring in "+films+":", actorchoice=actorchoice, filmchoice=filmchoice, actorselection=actorselection, filmselection=filmselection)
    


@app.route('/home/link', methods=['GET', 'POST']) # Delete function
def actor_film_associate():
    if request.method == "POST":
        details=request.form
        films=details['filmname']
        actors=details['actorname']
        if films != "- Choose a Film -" and actors != "- Choose an Actor -":
            cur = mysql.connection.cursor()
            cur.execute("INSERT IGNORE INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name=(%s)), (SELECT Actor_ID from Actors WHERE Actor_Name=(%s)));", [films, actors])
            mysql.connection.commit()
            cur.execute("select Actor_Name from Actors where Actor_ID in (select ActorID from Film_Actor where FilmID=(SELECT Film_ID from Films WHERE Film_Name=(%s)))", [films])
            mysql.connection.commit()
            selectactornames = cur.fetchall() #built in function to return a tuple, list or dictionary
            cur.execute("select Film_Name from Films where Film_ID in (select FilmID from Film_Actor where ActorID=(SELECT Actor_ID from Actors WHERE Actor_Name=(%s)))", [actors])
            mysql.connection.commit()
            selectfilmnames = cur.fetchall() 
            cur.execute("SELECT * FROM Films")
            mysql.connection.commit()
            filmnames = cur.fetchall() #built in function to return a tuple, list or dictionary
            cur.execute("SELECT * FROM Actors")
            mysql.connection.commit()
            actornames = cur.fetchall() #built in function to return a tuple, list or dictionary
            cur.close()

            actorchoice = []
            filmchoice = []
            actorselection = []
            filmselection = []

            for row in selectactornames:
                actorchoice.append(row) #adding each row from the database into a newly created list, info  
                     
            for row in actornames:
                actorselection.append(row) #adding each row from the database into a newly created list, info
            
            for row in filmnames:
                filmselection.append(row) #adding each row from the database into a newly created list, info  

            for row in selectfilmnames:
                filmchoice.append(row) #adding each row from the database into a newly created list, info 


            return render_template("index.html", name="Home",actor="Films starring "+actors+":", film="Actors starring in "+films+":", actorchoice=actorchoice, filmchoice=filmchoice, actorselection=actorselection, filmselection=filmselection)
    return redirect(url_for('home'))


@app.route('/home/dissociate', methods=['GET', 'POST']) # Delete function
def actor_film_dissociate():
    if request.method == "POST":
        details=request.form
        films=details['filmname']
        actors=details['actorname']
        
        cur = mysql.connection.cursor()
        cur.execute("DELETE Film_Actor FROM ((Film_Actor INNER JOIN Actors ON Film_Actor.ActorID = Actors.Actor_ID) INNER JOIN Films ON Film_Actor.FilmID = Films.Film_ID) WHERE Films.Film_Name=(%s) AND Actors.Actor_Name=(%s)", [films, actors])
        mysql.connection.commit()
        cur.execute("select Actor_Name from Actors where Actor_ID in (select ActorID from Film_Actor where FilmID=(SELECT Film_ID from Films WHERE Film_Name=(%s)))", [films])
        mysql.connection.commit()
        selectactornames = cur.fetchall() #built in function to return a tuple, list or dictionary
        cur.execute("select Film_Name from Films where Film_ID in (select FilmID from Film_Actor where ActorID=(SELECT Actor_ID from Actors WHERE Actor_Name=(%s)))", [actors])
        mysql.connection.commit()
        selectfilmnames = cur.fetchall() 
        cur.execute("SELECT * FROM Films")
        mysql.connection.commit()
        filmnames = cur.fetchall() #built in function to return a tuple, list or dictionary
        cur.execute("SELECT * FROM Actors")
        mysql.connection.commit()
        actornames = cur.fetchall() #built in function to return a tuple, list or dictionary
        cur.close()

        actorchoice = []
        filmchoice = []
        actorselection = []
        filmselection = []

        for row in selectactornames:
            actorchoice.append(row) #adding each row from the database into a newly created list, info  
                    
        for row in actornames:
            actorselection.append(row) #adding each row from the database into a newly created list, info
        
        for row in filmnames:
            filmselection.append(row) #adding each row from the database into a newly created list, info  

        for row in selectfilmnames:
            filmchoice.append(row) #adding each row from the database into a newly created list, info 
    
    if len(selectactornames)==0:
        actorchoice=[["There are no actors that star in this film"]] 
    
    if len(selectfilmnames)==0:
        filmchoice=[["This actor does not star in any films"]] 

    if films == "- Choose a Film -" and actors == "- Choose an Actor -":
        return redirect(url_for('home'))
    
    elif films != "- Choose a Film -" and actors == "- Choose an Actor -":
        return render_template("index.html", name="Home", film="Actors starring in "+films+":", actorchoice=actorchoice, filmchoice=filmchoice, actorselection=actorselection, filmselection=filmselection)

    elif films == "- Choose a Film -" and actors != "- Choose an Actor -":
        return render_template("index.html", name="Home", actor="Films starring "+actors+":", actorchoice=actorchoice, filmchoice=filmchoice, actorselection=actorselection, filmselection=filmselection)


    return render_template("index.html", name="Home",actor="Films starring "+actors+":", film="Actors starring in "+films+":", actorchoice=actorchoice, filmchoice=filmchoice, actorselection=actorselection, filmselection=filmselection)
    
@app.route('/home/delete/actors/all', methods=['GET', 'POST']) # Delete function
def actors_delete_all():
    if request.method == "POST":
        details=request.form
        actors=details['actorname']
        
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Films where Film_ID in (select FilmID from Film_Actor where ActorID=(SELECT Actor_ID from Actors WHERE Actor_Name=(%s)))", [actors])
        mysql.connection.commit()
        cur.execute("select Film_Name from Films where Film_ID in (select FilmID from Film_Actor where ActorID=(SELECT Actor_ID from Actors WHERE Actor_Name=(%s)))", [actors])
        mysql.connection.commit()
        selectfilmnames = cur.fetchall() 
        cur.execute("SELECT * FROM Films")
        mysql.connection.commit()
        filmnames = cur.fetchall() #built in function to return a tuple, list or dictionary
        cur.execute("SELECT * FROM Actors")
        mysql.connection.commit()
        actornames = cur.fetchall() #built in function to return a tuple, list or dictionary
        cur.close()

        filmchoice = []
        actorselection = []
        filmselection = []

                    
        for row in actornames:
            actorselection.append(row) #adding each row from the database into a newly created list, info
        
        for row in filmnames:
            filmselection.append(row) #adding each row from the database into a newly created list, info  

        for row in selectfilmnames:
            filmchoice.append(row) #adding each row from the database into a newly created list, info 
    
    if len(selectfilmnames)==0:
        filmchoice=[["This actor does not star in any films"]] 

    if actors == "- Choose an Actor -":
        return redirect(url_for('home'))
    
    return render_template("index.html", name="Home",actor="Films starring "+actors+":", filmchoice=filmchoice, actorselection=actorselection, filmselection=filmselection)


@app.route('/home/delete/films/all', methods=['GET', 'POST']) # Delete function
def films_delete_all():
    if request.method == "POST":
        details=request.form
        films=details['filmname']
        
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Actors where Actor_ID in (select ActorID from Film_Actor where FilmID=(SELECT Film_ID from Films WHERE Film_Name=(%s)))", [films])
        mysql.connection.commit()
        cur.execute("select Actor_Name from Actors where Actor_ID in (select ActorID from Film_Actor where FilmID=(SELECT Film_ID from Films WHERE Film_Name=(%s)))", [films])
        mysql.connection.commit()
        selectactornames = cur.fetchall() #built in function to return a tuple, list or dictionary
        cur.execute("SELECT * FROM Films")
        mysql.connection.commit()
        filmnames = cur.fetchall() #built in function to return a tuple, list or dictionary
        cur.execute("SELECT * FROM Actors")
        mysql.connection.commit()
        actornames = cur.fetchall() #built in function to return a tuple, list or dictionary
        cur.close()

        actorchoice = []
        actorselection = []
        filmselection = []

        for row in selectactornames:
            actorchoice.append(row) #adding each row from the database into a newly created list, info  
                    
        for row in actornames:
            actorselection.append(row) #adding each row from the database into a newly created list, info
        
        for row in filmnames:
            filmselection.append(row) #adding each row from the database into a newly created list, info  

    
    if len(selectactornames)==0:
        actorchoice=[["There are no actors that star in this film"]] 
    

    if films == "- Choose a Film -":
        return redirect(url_for('home'))
    

    return render_template("index.html", name="Home", film="Actors starring in "+films+":", actorchoice=actorchoice, actorselection=actorselection, filmselection=filmselection)


@app.route('/home/create/many', methods=['GET', 'POST']) # Delete function
def add_many():
    if request.method == "POST":
        details=request.form
        films=details['filmname']
        actors=details['actorname']
        if films != "" and actors != "":
            actornames=re.split("\s*;\s*", actors)
            filmnames=re.split("\s*;\s*", films)
            cur = mysql.connection.cursor()
            for i in range(len(actornames)):
                n = re.sub("^\s*", "", actornames[i])
                cur.execute("INSERT IGNORE INTO Actors (Actor_Name) VALUES (%s)", [n])
                mysql.connection.commit()
                for j in range(len(filmnames)):
                    m = re.sub("^\s*", "", filmnames[j])
                    cur.execute("INSERT IGNORE INTO Films (Film_Name) VALUES (%s)", [m])
                    mysql.connection.commit()
                    cur.execute("INSERT IGNORE INTO Film_Actor VALUES ((SELECT Film_ID from Films WHERE Film_Name=(%s)), (SELECT Actor_ID from Actors WHERE Actor_Name=(%s)));", [m, n])
                    mysql.connection.commit()
            cur.execute("select Actor_Name from Actors where Actor_ID in (select ActorID from Film_Actor where FilmID=(SELECT Film_ID from Films WHERE Film_Name=(%s)))", [films])
            mysql.connection.commit()
            selectactornames = cur.fetchall() #built in function to return a tuple, list or dictionary
            cur.execute("select Film_Name from Films where Film_ID in (select FilmID from Film_Actor where ActorID=(SELECT Actor_ID from Actors WHERE Actor_Name=(%s)))", [actors])
            mysql.connection.commit()
            selectfilmnames = cur.fetchall() 
            cur.execute("SELECT * FROM Films")
            mysql.connection.commit()
            filmnames = cur.fetchall() #built in function to return a tuple, list or dictionary
            cur.execute("SELECT * FROM Actors")
            mysql.connection.commit()
            actornames = cur.fetchall() #built in function to return a tuple, list or dictionary
            cur.close()

            actorchoice = []
            filmchoice = []
            actorselection = []
            filmselection = []

            for row in selectactornames:
                actorchoice.append(row) #adding each row from the database into a newly created list, info  
                     
            for row in actornames:
                actorselection.append(row) #adding each row from the database into a newly created list, info
            
            for row in filmnames:
                filmselection.append(row) #adding each row from the database into a newly created list, info  

            for row in selectfilmnames:
                filmchoice.append(row) #adding each row from the database into a newly created list, info 


            return render_template("index.html", name="Home",actor="Films starring "+actors+":", film="Actors starring in "+films+":", actorchoice=actorchoice, filmchoice=filmchoice, actorselection=actorselection, filmselection=filmselection)
    return redirect(url_for('home'))


######################################################################################################################################################################
###########################################################################     ACTORS     ###########################################################################
######################################################################################################################################################################

@app.route('/actors', methods=['GET', 'POST']) # Read Function
def actors():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Actors")
    mysql.connection.commit()
    actornames = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()

    actorselection = []

    for row in actornames:
        actorselection.append(row) #adding each row from the database into a newly created list, info  

    return render_template("actors.html", name="Actor Database", actorselection=actorselection)

@app.route('/actors/create', methods=['GET', 'POST']) # Create function
def actors_create():
    if request.method == "POST":
        details=request.form
        name=details['name']
        if name != "":
            x=re.split("\s*;\s*", name)
            cur = mysql.connection.cursor()
            for i in range(len(x)):
                n = re.sub("^\s*", "", x[i])
                cur.execute("INSERT IGNORE INTO Actors (Actor_Name) VALUES (%s)", [n])
            mysql.connection.commit()
            cur.close()

    return redirect(url_for('actors'))


@app.route('/actors/delete', methods=['GET', 'POST']) # Delete function
def actors_delete():
    if request.method == "POST":
        details=request.form
        actors=details['actors']
        if actors != "- Choose an Actor -":
            cur=mysql.connection.cursor()
            cur.execute("DELETE Actors, Film_Actor FROM Actors INNER JOIN Film_Actor ON Actors.Actor_ID = Film_Actor.ActorID WHERE Actors.Actor_Name=(%s)", [actors])
            cur.execute("DELETE FROM Actors where Actor_Name=(%s)", [actors]) #deletes films that aren't in the joining table
            mysql.connection.commit()
            cur.close()
    
    return redirect(url_for('actors'))
    
 

@app.route('/actors/update', methods=['GET', 'POST']) # Update function
def actors_update():
    if request.method == "POST":
        details=request.form
        fromname=details['initialname']
        toname=details['finalname']
        if fromname != "- Choose an Actor -":
            cur = mysql.connection.cursor()
            toname = re.sub("^\s*", "", toname)
            cur.execute("UPDATE Actors SET Actor_Name=(%s) WHERE Actor_Name=(%s)", [toname, fromname])
            mysql.connection.commit()
            cur.close()

    return redirect(url_for('actors'))


#######################################################################################################################################################################
############################################################################     FILMS     ############################################################################
#######################################################################################################################################################################


@app.route('/films', methods=['GET', 'POST']) # Read Function
def films():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Films")
    mysql.connection.commit()
    filmnames = cur.fetchall() #built in function to return a tuple, list or dictionary
    cur.close()

    filmselection = []

    for row in filmnames:
        filmselection.append(row) #adding each row from the database into a newly created list, info  

    return render_template("films.html", name="Film Database", filmselection=filmselection)

@app.route('/films/create', methods=['GET', 'POST']) # Create function
def films_create():
    if request.method == "POST":
        details=request.form
        name=details['name']
        if name != "":
            x=re.split("\s*;\s*", name)
            cur = mysql.connection.cursor()
            for i in range(len(x)):
                n = re.sub("^\s*", "", x[i])
                cur.execute("INSERT IGNORE INTO Films (Film_Name) VALUES (%s)", [n])
            mysql.connection.commit()
            cur.close()

    return redirect(url_for('films'))


@app.route('/films/delete', methods=['GET', 'POST']) # Delete function
def films_delete():
    if request.method == "POST":
        details=request.form
        films=details['films']
        if actors != "- Choose a Film -":
            cur=mysql.connection.cursor()
            cur.execute("DELETE Films, Film_Actor FROM Films INNER JOIN Film_Actor ON Films.Film_ID = Film_Actor.FilmID WHERE Films.Film_Name=(%s)", [films]) #deletes film from both tables
            cur.execute("DELETE FROM Films where Film_Name=(%s)", [films]) #deletes films that aren't in the joining table
            mysql.connection.commit()
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
            toname = re.sub("^\s*", "", fromname)
            cur.execute("UPDATE Films SET Film_Name=(%s) WHERE Film_Name=(%s)", [toname, fromname])
            mysql.connection.commit()
            cur.close()

    return redirect(url_for('films'))


#######################################################################################################################################################################
############################################################################     MISC.     ############################################################################
#######################################################################################################################################################################

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)