from flask import Flask, redirect, url_for, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/gear")
def gear_page():
    return render_template('gear.html')

@app.route("/people")
def people():

    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    c.execute("select * from people where id >= 1")
    result = c.fetchall()
    conn.close()
    return render_template('people.html', posts = result)

@app.route("/event")
def event():
    return render_template('event.html')

@app.route("/guide")
def guide():
    return render_template('guide.html')


if __name__ == "__main__":
    app.run(debug = True)
