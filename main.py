from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')



@app.route("/gear")
def gear_page():
    return render_template('gear.html')

@app.route("/gear", methods = ['POST'])
def gear_post():

    if request.method == 'POST' and "search_bar" in request.form:

        search = request.form['search_bar']

        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select * from one where name LIKE '%"+ search +"%'")

        result = c.fetchall()
        conn.close()
        return render_template('gear.html', tests = result)

    return render_template('gear.html')



@app.route("/people")
def people():

    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    c.execute("select * from people where id >= 1")
    result = c.fetchall()
    conn.close()
    return render_template('people.html', results = result)




@app.route("/event")
def event():
    return render_template('event.html')




@app.route("/guide")
def guide():
    return render_template('guide.html')




if __name__ == "__main__":
    app.run(debug = True)
