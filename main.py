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

    if request.method == 'POST' and "search_bar" in request.form:
        search = request.form['search_bar']
        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select * from snowbaord where name LIKE '%"+ search +"%'")
        result = c.fetchall()
        conn.close()
        return render_template('gear_snowbaord.html', tests = result)

    if request.method == 'POST' and "Burton" in request.form:
        brand_search = brand_search + 1
        search = "Burton"
        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select id from snowbaord where brand = ?",(search,))
        brand_search_ids = brand_search_ids + c.fetchall()
        conn.close()


    if request.method == 'POST' and "Salomon" in request.form:
        brand_search = brand_search + 1
        search = "Salomon"
        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select id from snowbaord where brand = ?",(search,))
        brand_search_ids = brand_search_ids + c.fetchall()
        conn.close()


    if request.method == 'POST' and "Lib_Tech" in request.form:
        brand_search = brand_search + 1
        search = "Lib_Tech"
        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select id from snowbaord where brand = ?",(search,))
        brand_search_ids = brand_search_ids + c.fetchall()
        conn.close()


    if request.method == 'POST' and "Jones_Snowboards" in request.form:
        brand_search = brand_search + 1
        search = "Jones_Snowboards"
        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select id from snowbaord where brand = ?",(search,))
        brand_search_ids = brand_search_ids + c.fetchall()
        conn.close()


    if request.method == 'POST' and "Gnu" in request.form:
        brand_search = brand_search + 1
        search = "Gnu"
        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select id from snowbaord where brand = ?",(search,))
        brand_search_ids = brand_search_ids + c.fetchall()
        conn.close()

    if request.method == 'POST' and "yellow" in request.form:
        colour_search = colour_search + 1
        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select id from snowbaord where id =(select snowbaord_id from snowbaord_colour where colour_id =5)")
        colour_search_ids = colour_search_ids + c.fetchall()
        conn.close()

    if request.method == 'POST' and "140" in request.form:
        size_search = size_search + 1
        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select id from snowbaord where size = 140")
        size_search_ids = size_search_ids + c.fetchall()
        conn.close()

    if request.method == 'POST' and "300" in request.form:
        price_search = price_search + 1
        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select id from snowbaord where price <=300")
        price_search_ids = price_search_ids + c.fetchall()
        conn.close()




    return render_template('gear_snowbaord.html', tests = result, price_search_ids = price_search_ids,  brand_search_ids = brand_search_ids, colour_search_ids = colour_search_ids, size_search_ids = size_search_ids )










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
