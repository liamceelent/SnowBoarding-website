from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3
from func import database, filterbrand, filtercolor, filtersize
import os
import hashlib



app = Flask(__name__)

app.config['SECRET_KEY'] = 'super secret key'


@app.route("/")
def home():
    if 'username' in session:
        stat = "you are logged in as", session['username']
        return render_template('home.html', stat = stat)
    else:
        return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/login", methods = ['POST', 'GET'])
def create_acc():

    if request.method == 'POST' and "create_name" in request.form:

        name = request.form['create_name']
        password = request.form['create_pass']

        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

        conn = sqlite3.connect("snowbaord.db")
        brand = []
        brand.insert(0, name)
        brand.insert(1, salt)
        brand.insert(2, key)
        brand = tuple(brand)

        query = "INSERT INTO user(name, salt, key) VALUES(?, ?, ?)"

        c = conn.cursor()
        c.execute(query, brand)
        conn.commit()
        conn.close()
        print(query,brand)

        return render_template('login.html')

    if request.method == 'POST' and "name" in request.form:

        name = request.form['name']
        password = request.form['pass']

        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select salt, key from user where name = ?",(name,))
        result = c.fetchall()
        conn.close()
        print(result)

        if not result:
            stat = "wrong user name mate"
            return render_template('login.html', stat=stat)
        else:
            salt = result[0][0]
            key = result[0][1]
            new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
            if key == new_key:
                session['key_name'] = 123312
                session['username'] = name
                return redirect(url_for("home"))
            else:
                stat = "wrong user name mate"
                return render_template('login.html', stat=stat)

    if request.method == 'POST' and "name" in request.form:

        name = request.form['name']
        password = request.form['pass']

        a = User.query.filter_by(name=name).first()
        if a is not None:
            salt = a.salt
            key = a.key
            new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
            if key == new_key:
                return redirect(url_for("home"))

            else:
                stat = "wrong user name mate"
                return render_template('login.html', stat=stat)
        else:
            stat = "wrong user name mate"
            return render_template('login.html', stat=stat)




@app.route("/gear", methods = ['POST', 'GET'])
def gear_page():
    if 'key_name' in session:
        session_var = session['key_name']
        return render_template('gear.html')
    else:
        return render_template('home.html')





@app.route("/gear_snowbinding", methods = ['POST', 'GET'])
def gear_snowbinding():

    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    c.execute("select * from snowbinding where id >= 1")
    result = c.fetchall()
    conn.close()
    # search bar for snwobinding

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

    #prices

    l200 = request.form.get('200')
    l300 = request.form.get('300')
    l400 = request.form.get('400')
    l500 = request.form.get('500')
    l600 = request.form.get('600')
    g600 = request.form.get('600+')

    # search bar code
    if search_bar is not None:
        query = "select * from snowbaord where name LIKE '%"+ search_bar +"%'" # so anything that has a like term shows
        result = database(query)
        return render_template('gear_snowbaord.html', tests = result)

    bcount = 0 # counting how many brand request forms we have
    ccount = 0 # counting how many color request forms we have
    scount = 0 # counting how many size request forms we have
    pcount = 0 # counting how many price request forms we have

    #counting the request forms brands
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
    #counting the request forms color
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
    #counting the request forms price
    if l200 is not None:
        pcount += 1
    if l300 is not None:
        pcount += 1
    if l400 is not None:
        pcount += 1
    if l500 is not None:
        pcount += 1
    if l600 is not None:
        pcount += 1
    if g600 is not None:
        pcount += 1

# braqndssssssssssssssssssssssssssssssss

    fcount = 0 # using this to see how many brands have been placed in the query

    query = "SELECT * FROM snowbaord "

    if bcount or ccount or scount or pcount > 0:
        if fcount == 0:
            query += "WHERE "

    if bcount > 1:
        query += "(" # if there is more than one brand to be filtered


    if Burton is not None: # checking if the reqeust form is empty
        query += filterbrand(fcount,bcount,"brand = 'Burton'")
        fcount += 1

    if Salomon is not None:
        query += filterbrand(fcount,bcount,"brand = 'Salomon'")
        fcount += 1

    if Lib_Tech is not None:
        query += filterbrand(fcount,bcount,"brand = 'Lib_Tech'")
        fcount += 1

    if Jones_Snowboards is not None:
        query += filterbrand(fcount,bcount,"brand = 'Jones_Snowboards'")
        fcount += 1

    if Gnu is not None:
        query += filterbrand(fcount,bcount,"brand = 'Gnu'")
        fcount += 1

    if bcount >1:
        query += ")"

# colorsssssssssssssssssssssss

    fcount = 0 # counting how many color have been put into the query

    if bcount >= 1:
        if ccount > 1:
            query += "AND (" #checks if there has been a brand and if there is more than one color

    if bcount == 0:
        if ccount >1:
            query += "(" # if no brand but more that one color


    if yellow is not None: # checking weather form is empty or not
        query += filtercolor(lcount, bcount, ccount,"id =(select snowbaord_id from snowbaord_colour where colour_id =1) ")
        lcount+=1

    if blue is not None:
        query += filtercolor(lcount, bcount, ccount,"id =(select snowbaord_id from snowbaord_colour where colour_id =2) ")
        lcount+=1


    if orange is not None:
        query += filtercolor(lcount, bcount, ccount,"id =(select snowbaord_id from snowbaord_colour where colour_id =7) ")
        lcount+=1

    if pink is not None:
        query += filtercolor(lcount, bcount, ccount,"id =(select snowbaord_id from snowbaord_colour where colour_id =8) ")
        lcount+=1


    if other is not None:
        query += filtercolor(lcount, bcount, ccount,"id =(select snowbaord_id from snowbaord_colour where colour_id =3) ")
        lcount+=1


    if white is not None:
        query += filtercolor(lcount, bcount, ccount,"id =(select snowbaord_id from snowbaord_colour where colour_id =4) ")
        lcount+=1


    if black is not None:
        query += filtercolor(lcount, bcount, ccount,"id =(select snowbaord_id from snowbaord_colour where colour_id =5) ")
        lcount+=1


    if red is not None:
        query += filtercolor(lcount, bcount, ccount,"id =(select snowbaord_id from snowbaord_colour where colour_id =6) ")
        lcount+=1


    if ccount > 1:
        query += ")"

    print(query)#debug

# sizesssssssssssssssssssssssssssssssss
    gcount = 0

    if bcount or ccount >= 1: # checking if and is neccessary and brackets
            if scount > 1:
                query += "AND ("

    if one_forty is not None: # checking if the form is empty
        query += filtersize(bcount,ccount,scount,gcount,"size = 140 " )
        gcount +=1

    if one_forty_two is not None:
        query += filtersize(bcount,ccount,scount,gcount,"size = 142 " )
        gcount +=1

    if one_forty_four is not None:
        query += filtersize(bcount,ccount,scount,gcount,"size = 144 " )
        gcount +=1

    if one_forty_six is not None:
        query += filtersize(bcount,ccount,scount,gcount,"size = 146 " )
        gcount +=1

    if one_forty_eight is not None:
        query += filtersize(bcount,ccount,scount,gcount,"size = 148 " )
        gcount +=1

    if bcount or ccount >= 1:
        if scount >1:
            query += ")"

# price

    kcount = 0 # counting if there has been a query
    if pcount > 0:
        if bcount or ccount or scount > 0:
            query += " AND "

    if g600 is not None: # checking if its not none
        query += filterprice(bcount,ccount,scount,gcount,"price > 600")
        gcount += 1


    if g600 is None:
        if l600 is not None:
            if kcount == 0:
                query += "price <= 600"
                kcount += 1

    if g600 or l600  is None:
        if l500 is not None:
            if kcount == 0:
                query += "price <= 500"
                kcount += 1

    if g600 or l600 or l500  is None:
        if l400 is not None:
            if kcount ==0:
                query += "price <= 400"
                kcount += 1


    if g600 or l600 or l500 or l400 is None:
        if l300 is not None:
            if kcount == 0:
                query += "price <= 300"
                kcount += 1

    if g600 or l600 or l500 or l400 or l300 is None:
        if l200 is not None:
            if kcount == 0:
                query += "price <= 200"
                kcount += 1


    print(query) #debug
    print(scount, gcount)#debug

    conn = sqlite3.connect('snowbaord.db')
    c = conn.cursor()
    c.execute(query)
    test = c.fetchall()
    conn.close()
    return render_template("gear_snowbaord.html", tests = test)




    return render_template('gear_snowbaord.html', tests = result)










@app.route("/gear_clothes", methods = ['POST', 'GET'])
def gear_clothes():

    result = database("select * from clothes where id >= 1")

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
def forms():
    return render_template('forms.html')

@app.route("/forms", methods = ['POST', 'GET'])
def forms_post():

    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    c.execute("select * from formpost")
    post = c.fetchall()
    conn.close()

    if request.method == 'POST' and "blogpost" in request.form:
        blogpost = request.form['blogpost']

        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        sql = "INSERT INTO formpost (post, user, test) VALUES (?, ?, ?)"
        val = (blogpost, session['username'], "11")
        c.execute(sql, val)
        conn.commit()
        conn.close()
        stat = "added"

        return render_template('forms.html', stat=stat, post = post)


    return render_template('forms.html', post = post)


@app.route("/guide")
def guide():
    return render_template('guide.html')




if __name__ == "__main__":
    app.run(debug = True)
