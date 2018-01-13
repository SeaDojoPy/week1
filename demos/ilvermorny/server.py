from flask import Flask, render_template, redirect, request, session
from mysqlconnector import MySQLConnector
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

DB = MySQLConnector(app, "ilvermorny")   


@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/houses')
def houses():
    query_string = "SELECT ilvermorny.students.name AS student, ilvermorny.houses.name AS house FROM ilvermorny.students JOIN ilvermorny.houses ON ilvermorny.students.house_id=ilvermorny.houses.id;"
    results = DB.query_db(query_string)
    print results
    return render_template('houses.html', context=results)

@app.route('/sortify', methods=['POST'])
def sortify():
    name = request.form['name']
    house = random.randint(1,4)
    data = {
        'name': name,
        'house': house
    }
    session['data'] = data
    query_string = "INSERT INTO students (name, house_id) VALUES (:name, :house);"
    DB.query_db(query_string, data)
    return redirect('/houses')


app.run(debug=True)