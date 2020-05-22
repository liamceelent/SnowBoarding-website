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
    test = c.fetchall()
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

    # sizes

    one_forty = request.form.get('140')
    one_forty_two = request.form.get('142')
    one_forty_four = request.form.get('144')
    one_forty_six = request.form.get('146')
    one_forty_eight = request.form.get('148')

    if search_bar is not None:
        query = "select * from snowbaord where name LIKE '%"+ search_bar +"%'"
        result = database(query)
        return render_template('gear_snowbaord.html', tests = result)

    bcount = 0
    ccount = 0
    scount = 0

    if Burton is not None:
        bcount += 1
    if Salomon is not None:
        bcount += 1
    if Lib_Tech is not None:
        bcount += 1
    if Jones_Snowboards is not None:
        bcount += 1
    if Gnu is not None:
        bcount += 1

    if blue is not None:
        ccount += 1
    if red is not None:
        ccount += 1
    if orange is not None:
        ccount += 1
    if pink is not None:
        ccount += 1
    if white is not None:
        ccount += 1
    if black is not None:
        ccount += 1
    if yellow is not None:
        ccount += 1
    if other is not None:
        ccount += 1

    if one_forty is not None:
        scount += 1
    if one_forty_two is not None:
        scount += 1
    if one_forty_four is not None:
        scount += 1
    if one_forty_six is not None:
        scount += 1
    if one_forty_eight is not None:
        scount += 1

# braqndssssssssssssssssssssssssssssssss
    fcount = 0

    query = "SELECT * FROM snowbaord "
    if bcount or ccount or scount > 0:
        if fcount == 0:
            query += "WHERE "

    if bcount > 1:
        query += "("


    if Burton is not None:
        if fcount > 0:
            if bcount == 1:
                query += "AND "
        if fcount > 0:
            if bcount >1:
                query += "OR "
        query += "brand = 'Burton' " # Add Filter
        fcount += 1

    if Salomon is not None:
        if fcount > 0:
            if bcount == 1:
                query += "AND "
        if fcount > 0:
            if bcount >1:
                query += "OR "
        query += "brand = 'Salomon' " # Add Filter
        fcount += 1

    if Lib_Tech is not None:
        if fcount > 0:
            if bcount == 1:
                query += "AND "
        if fcount > 0:
            if bcount >1:
                query += "OR "
        query += "brand = 'Lib_Tech' " # Add Filter
        fcount += 1

    if Jones_Snowboards is not None:
        if fcount > 0:
            if bcount == 1:
                query += "AND "
        if fcount > 0:
            if bcount >1:
                query += "OR "
        query += "brand = 'Jones_Snowboards' " # Add Filter
        fcount += 1

    if Gnu is not None:
        if fcount > 0:
            if bcount == 1:
                query += "AND "
        if fcount > 0:
            if bcount >1:
                query += "OR "
        query += "brand = 'Gnu'" # Add Filter
        fcount += 1

    if bcount >1:
        query += ")"

# colorsssssssssssssssssssssss
    lcount = 0

    if bcount >= 1:
        if ccount > 1:
            query += "AND ("

    if bcount == 0:
        if ccount >1:
            query += "("


    if yellow is not None:
        if bcount >= 1:
            if ccount == 1:
                    query += "AND "
        if lcount > 0:
            if ccount > 1:
                query += "OR "
        query += "id =(select snowbaord_id from snowbaord_colour where colour_id =1) " # Add Filter
        lcount += 1

    if blue is not None:
        if bcount >= 1:
            if ccount == 1:
                    query += "AND "
        if lcount > 0:
            if ccount > 1:
                query += "OR "
        query += "id =(select snowbaord_id from snowbaord_colour where colour_id =2) " # Add Filter
        lcount += 1

    if orange is not None:
        if bcount >= 1:
            if ccount == 1:
                query += "AND "
        if lcount > 0:
            if lcount > 1:
                query += "OR "
        query += "id =(select snowbaord_id from snowbaord_colour where colour_id =7) " # Add Filter
        fcount += 1

    if pink is not None:
        if bcount >= 1:
            if ccount == 1:
                query += "AND "
        if lcount > 0:
            if ccount > 1:
                query += "OR "
        query += "id =(select snowbaord_id from snowbaord_colour where colour_id =8) " # Add Filter
        lcount += 1

    if other is not None:
        if bcount >= 1:
            if ccount == 1:
                query += "AND "
        if lcount > 0:
            if ccount > 1:
                query += "OR "
        query += "id =(select snowbaord_id from snowbaord_colour where colour_id =3) " # Add Filter
        lcount += 1

    if white is not None:
        if bcount >= 1:
            if ccount == 1:
                query += "AND "
        if lcount > 0:
            if ccount > 1:
                query += "OR "
        query += "id =(select snowbaord_id from snowbaord_colour where colour_id =4) " # Add Filter
        lcount += 1

    if black is not None:
        if bcount >= 1:
            if ccount == 1:
                query += "AND "
        if lcount > 0:
            if ccount > 1:
                query += "OR "
        query += "id =(select snowbaord_id from snowbaord_colour where colour_id =5) " # Add Filter
        lcount += 1

    if red is not None:
        if bcount >= 1:
            if ccount == 1:
                query += "AND "
        if lcount > 0:
            if ccount > 1:
                query += "OR "
        query += "id =(select snowbaord_id from snowbaord_colour where colour_id =6) " # Add Filter
        lcount += 1

    if ccount > 1:
        query += ")"

    print(query)

# sizesssssssssssssssssssssssssssssssss
    gcount = 0

    if bcount or ccount >= 1:
            if scount > 1:
                query += "AND ("

    if one_forty is not None:
        if bcount or ccount >= 1:
            if scount == 1:
                query += " AND "
        if gcount > 0:
            if scount > 1:
                query += "OR "
        query += "size = 140 " # Add Filter
        gcount += 1

    if one_forty_two is not None:
        if bcount or ccount >= 1:
            if scount == 1:
                query += " AND "
        if gcount > 0:
            if scount > 1:
                query += "OR "
        query += "size = 142 " # Add Filter
        gcount += 1

    if one_forty_four is not None:
        if bcount or ccount >= 1:
            if scount == 1:
                query += " AND "
        if gcount > 0:
            if scount > 1:
                query += "OR "
        query += "size = 144 " # Add Filter
        gcount += 1

    if one_forty_six is not None:
        if bcount or ccount >= 1:
            if scount == 1:
                query += " AND "
        if gcount > 0:
            if scount > 1:
                query += "OR "
        query += "size = 146 " # Add Filter
        gcount += 1

    if one_forty_eight is not None:
        if bcount or ccount >= 1:
            if scount == 1:
                query += " AND "
        if gcount > 0:
            if scount > 1:
                query += "OR "
        query += "size = 148 " # Add Filter
        gcount += 1

    if bcount or ccount >= 1:
        if scount >1:
            query += ")"


    print(query)
    print(scount, gcount)
    # Connect to databse and preform query
    conn = sqlite3.connect('snowbaord.db')
    c = conn.cursor()
    c.execute(query)
    test = c.fetchall()
    conn.close()
    return render_template("gear_snowbaord.html", tests = test)




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
