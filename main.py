from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')



@app.route("/gear")
def gear_page():
    return render_template('gear.html')

@app.route("/gear", methods = ['POST', 'GET'])
def gear_post():

    result = []

    if request.method == 'POST' and "search_bar" in request.form:

        search = request.form['search_bar']

        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select * from snowbaord where name LIKE '%"+ search +"%'")
        result_1 = c.fetchall()
        c.execute("select * from snowbinding where name LIKE '%"+ search +"%'")
        result_2 = c.fetchall()
        c.execute("select * from snow_boots where name LIKE '%"+ search +"%'")
        result_3 = c.fetchall()
        c.execute("select * from clothes where name LIKE '%"+ search +"%'")
        result_4 = c.fetchall()
        conn.close()
        return render_template('gear.html', tests = result_1+result_2+result_3+result_4)


    if request.method == 'POST' and "snowbaord" in request.form:

        request.form['snowbaord']
        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select * from snowbaord where id >= 1")

        result = result + c.fetchall()
        conn.close()


    if request.method == 'POST' and "snowboots" in request.form:

        request.form['snowboots']
        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select * from snow_boots where id >= 1")

        result = result + c.fetchall()
        conn.close()


    if request.method == 'POST' and "clothes" in request.form:

        request.form['clothes']
        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select * from clothes where id >= 1")

        result = result + c.fetchall()
        conn.close()


    if request.method == 'POST' and "snowbinding" in request.form:

        request.form['snowbinding']
        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select * from snowbinding where id >= 1")

        result = result + c.fetchall()
        conn.close()


    return render_template('gear.html', tests = result)

@app.route("/gear_snowbinding")
def gear_snowbinding():
    return render_template('gear_snowbinding.html')

@app.route("/gear_snowbaord")
def gear_snowbaord():
    return render_template('gear_snowbaord.html')

@app.route("/gear_clothes")
def gear_clothes():
    return render_template('gear_clothes.html')

@app.route("/gear_snow_boots")
def gear_snow_boots():
    return render_template('gear_snow_boots.html')

@app.route("/gear_click")
def gear_click():

    search_id = request.args.get('search_id')
    table = request.args.get('table')

    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    c.execute("select * from snowbaord where name = ?",(search_id,))
    result = c.fetchall()
    conn.close()

    return render_template('gearspec.html', name = search_id, result = result, table= table)

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
