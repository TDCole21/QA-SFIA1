from flask import Flask
from flask_mysqldb import MySQL
import os

app=Flask(__name__)

mysql=MySQL(app)

app.config['MYSQL_HOST']=os.environ['MYSQLHOST']
app.config['MYSQL_USER']=os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD']=os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB']=os.environ['MYSQLDB']


def test_select():                                               #select test
    with app.app_context():
        cur= mysql.connection.cursor()
        num_of_records=cur.execute('SELECT * FROM Films')    #test made on the table that's not used for CRUD 
        mysql.connection.commit()
        cur.close()
        assert 28 == num_of_records                             #checks if the number of records in the database matches the number of entries expected to have in the table

def test_insert():                                              #insert test
    with app.app_context():
        cur= mysql.connection.cursor()
        cur.execute('SELECT * FROM Actors')                   #tests made on the table used for CRUD
        num_of_records=cur.fetchall()
        cur.execute('INSERT INTO Actors (Actor_Name) VALUES ("z-test")')  #inserts at an autoincrement ID the value 'test'
        mysql.connection.commit()
        cur.execute('SELECT * FROM Actors')
        new_num_records=cur.fetchall()
        cur.close()
    assert num_of_records[len(num_of_records)-1] != new_num_records[len(new_num_records)-1]


    
def test_delete():                                              #delete test
    with app.app_context():
        cur= mysql.connection.cursor()
        cur.execute('SELECT * FROM Actors')                   #tests made on the table used for CRUD
        num_of_records=cur.fetchall()
        cur.execute('DELETE FROM Actors WHERE Actor_ID= %s', [int(num_of_records[len(num_of_records)-1][0])])  #delete all entries in the table that have the name 'test'
        mysql.connection.commit()
        cur.execute('SELECT * FROM Actors')
        new_num_records=cur.fetchall()
        cur.close()
    assert num_of_records[len(num_of_records)-1][0] != new_num_records[len(new_num_records)-1][0]