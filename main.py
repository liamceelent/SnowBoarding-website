from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3
from func import database

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')



@app.route("/gear")
def gear_page():
    return render_template('gear.html')

@app.route("/gear", methods = ['POST', 'GET'])
def gear_post():

    return render_template('gear.html')


@app.route("/gear_snowbinding", methods = ['POST', 'GET'])
def gear_snowbinding():

    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    c.execute("select * from snowbinding where id >= 1")
    result = c.fetchall()
    conn.close()

    if request.method == 'POST' and "search_bar" in request.form:
        search = request.form['search_bar']
        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select * from snowbinding where name LIKE '%"+ search +"%'")
        result = c.fetchall()

        conn.close()
        return render_template('gear_snowbinding.html', tests = result)
    return render_template('gear_snowbinding.html', tests = result)






@app.route("/gear_snowbaord", methods = ['POST', 'GET'])
def gear_snowbaord():

    brand_search = 0
    brand_search_ids = []
    colour_search = 0
    colour_search_ids = []
    size_search = 0
    size_search_ids = []
    price_search = 0
    price_search_ids = []

    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    c.execute("select * from snowbaord where id >= 1")
    result = c.fetchall()
    conn.close()

    search_bar = request.form.get('search_bar')

    #brands request

    Burton = request.form.get('Burton')
    Salomon = request.form.get('Salomon')
    Lib_Tech = request.form.get('Lib_Tech')
    Jones_Snowboards = request.form.get('Jones_Snowboards')
    Gnu = request.form.get('Gnu')

    #colour
    blue = request.form.get('blue')
    red = request.form.get('red')
    orange = request.form.get('orange')
    pink = request.form.get('pink')
    white = request.form.get('white')
    black = request.form.get('black')
    yellow = request.form.get('yellow')
    other = request.form.get('other')
    green = request.form.get('green')


    #price


    #size


    if search_bar is not None:
        query = "select * from snowbaord where name LIKE '%"+ search_bar +"%'"
        result = database(query)
        return render_template('gear_snowbaord.html', tests = result)

    fcount = 0
    query = "SELECT * FROM snowbaord "

    # Add "WHERE" if a filter has been applied
    if Burton or Salomon or Lib_Tech or Jones_Snowboards or Gnu or yellow or blue or red or orange or pink or white or black or other  is not None:
        query += "WHERE "

    # Check what filters have been applied
    if Burton is not None:
        if fcount > 0:
            query += "AND " # Check if "AND" is neccessary
        query += "brand = 'Burton' " # Add Filter
        fcount += 1

    if Salomon is not None:
        if fcount > 0:
            query += "AND " # Check if "AND" is neccessary
        query += "brand = 'Salomon' " # Add Filter
        fcount += 1

    if Lib_Tech is not None:
        if fcount > 0:
            query += "AND " # Check if "AND" is neccessary
        query += "brand = 'Lib_Tech' " # Add Filter
        fcount += 1

    if Jones_Snowboards is not None:
        if fcount > 0:
            query += "AND " # Check if "AND" is neccessary
        query += "brand = 'Jones_Snowboards' " # Add Filter
        fcount += 1

    if Gnu is not None:
        if fcount > 0:
            query += "AND " # Check if "AND" is neccessary
        query += "brand = 'Gnu'" # Add Filter
        fcount += 1

    if yellow is not None:
        if fcount > 0:
            query += "AND " # Check if "AND" is neccessary
        query += "id =(select snowbaord_id from snowbaord_colour where colour_id =1) " # Add Filter
        fcount += 1

    if blue is not None:
        if fcount > 0:
            query += "AND " # Check if "AND" is neccessary
        query += "id =(select snowbaord_id from snowbaord_colour where colour_id =2) " # Add Filter
        fcount += 1

    if orange is not None:
        if fcount > 0:
            query += "AND " # Check if "AND" is neccessary
        query += "id =(select snowbaord_id from snowbaord_colour where colour_id =7) " # Add Filter
        fcount += 1

    if pink is not None:
        if fcount > 0:
            query += "AND " # Check if "AND" is neccessary
        query += "id =(select snowbaord_id from snowbaord_colour where colour_id =8) " # Add Filter
        fcount += 1

    if other is not None:
        if fcount > 0:
            query += "AND " # Check if "AND" is neccessary
        query += "id =(select snowbaord_id from snowbaord_colour where colour_id =3) " # Add Filter
        fcount += 1

    if white is not None:
        if fcount > 0:
            query += "AND " # Check if "AND" is neccessary
        query += "id =(select snowbaord_id from snowbaord_colour where colour_id =4) " # Add Filter
        fcount += 1

    if black is not None:
        if fcount > 0:
            query += "AND " # Check if "AND" is neccessary
        query += "id =(select snowbaord_id from snowbaord_colour where colour_id =5) " # Add Filter
        fcount += 1

    if red is not None:
        if fcount > 0:
            query += "AND " # Check if "AND" is neccessary
        query += "id =(select snowbaord_id from snowbaord_colour where colour_id =6) " # Add Filter
        fcount += 1

    # Connect to databse and preform query
    conn = sqlite3.connect('snowbaord.db')
    c = conn.cursor()
    c.execute(query)
    bike = c.fetchall()
    conn.close()
    return render_template("gear_snowbaord.html", tests = bike)




    return render_template('gear_snowbaord.html', tests = result)










@app.route("/gear_clothes", methods = ['POST', 'GET'])
def gear_clothes():

    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    c.execute("select * from clothes where id >= 1")
    result = c.fetchall()
    conn.close()

    if request.method == 'POST' and "search_bar" in request.form:
        search = request.form['search_bar']
        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select * from clothes where name LIKE '%"+ search +"%'")
        result = c.fetchall()
        conn.close()

        return render_template('gear_clothes.html', tests = result)
    return render_template('gear_clothes.html', tests = result)



@app.route("/gear_snow_boots", methods = ['POST', 'GET'])
def gear_snow_boots():

    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    c.execute("select * from snow_boots where id >= 1")
    result = c.fetchall()
    conn.close()

    if request.method == 'POST' and "search_bar" in request.form:
        search = request.form['search_bar']
        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select * from snow_boots where name LIKE '%"+ search +"%'")
        result = c.fetchall()
        conn.close()

        return render_template('gear_snow_boots.html', tests = result)
    return render_template('gear_snow_boots.html', tests = result)


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
    query = "select * from people where id >= 1"
    result = database(query)
    return render_template('people.html', results = result)




@app.route("/forms")
def event():
    return render_template('forms.html')




@app.route("/guide")
def guide():
    return render_template('guide.html')




if __name__ == "__main__":
    app.run(debug = True)
