from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'mydb')

@app.route('/')
def index():

    friends = mysql.query_db('SELECT * FROM myfriends')
    return render_template('index.html', all_friends = friends)



@app.route('/process', methods=['POST'])
def input():
    query = "INSERT INTO myfriends(name, age, created_at, updated_at)VALUES(:name, :age, NOW(), NOW())"

    data = {
        'name': request.form['name'],
        'age': request.form['age']
    }

    print data
    mysql.query_db(query,data)
    return redirect('/')

app.run(debug=True)

