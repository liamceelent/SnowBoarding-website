from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3
from func import database, filtersnowbaord
import os
import hashlib
import datetime


app = Flask(__name__)

app.config['SECRET_KEY'] = 'super secret key'

@app.route("/")
def home():
    if "username" in session:
        stat = "you are logged in as", session['username']
        return render_template('home.html', stat = stat)
    else:
        session['username'] = "guest"
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
                session["username"] = name
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

    return render_template('gear.html')






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

    query = filtersnowbaord(Burton,Salomon,Lib_Tech,Jones_Snowboards,Gnu,blue,red,\
    orange,pink,white,black,yellow,other,one_forty,one_forty_two,one_forty_four,\
    one_forty_six,one_forty_eight,l200,l300,l400,l500,l600,g600)

    conn = sqlite3.connect('snowbaord.db')# shorten
    c = conn.cursor()
    c.execute(query)
    test = c.fetchall()
    conn.close()
    return render_template("gear_snowbaord.html", tests = test)


@app.route("/gear_clothes", methods = ['POST', 'GET'])
def gear_clothes():

    result = database("select * from clothes where id >= 1")

    if request.method == 'POST' and "search_bar" in request.form:
        search = request.form['search_bar']
        conn = sqlite3.connect("snowbaord.db")# shorten
        c = conn.cursor()
        c.execute("select * from clothes where name LIKE '%"+ search +"%'")
        result = c.fetchall()
        conn.close()

        return render_template('gear_clothes.html', tests = result)
    return render_template('gear_clothes.html', tests = result)



@app.route("/gear_snow_boots", methods = ['POST', 'GET'])
def gear_snow_boots():

    conn = sqlite3.connect("snowbaord.db")# shorten
    c = conn.cursor()
    c.execute("select * from snow_boots where id >= 1")
    result = c.fetchall()
    conn.close()

    if request.method == 'POST' and "search_bar" in request.form:
        search = request.form['search_bar']
        conn = sqlite3.connect("snowbaord.db")# shorten
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

    conn = sqlite3.connect("snowbaord.db")# shorten
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

    conn = sqlite3.connect("snowbaord.db")# shorten
    c = conn.cursor()
    c.execute("select * from formpost")
    result = c.fetchall()
    conn.close()

    conn = sqlite3.connect("snowbaord.db")# shorten
    c = conn.cursor()
    c.execute("select * from user where name =?",(session['username'],))
    personal_stat = c.fetchall()
    conn.close()

    conn = sqlite3.connect("snowbaord.db") # shorten
    c = conn.cursor()
    c.execute("SELECT user,dislikes FROM formpost ORDER BY dislikes DESC LIMIT 10")
    worst_posts = c.fetchall()
    conn.close()

    conn = sqlite3.connect("snowbaord.db") # shorten
    c = conn.cursor()
    c.execute("SELECT user,likes FROM formpost ORDER BY likes DESC LIMIT 10")
    best_posts = c.fetchall()
    conn.close()

    conn = sqlite3.connect("snowbaord.db") # shorten
    c = conn.cursor()
    c.execute("SELECT name,post FROM user ORDER BY post DESC LIMIT 10")
    top_posters = c.fetchall()
    conn.close()

    return render_template('forms.html', result = result, stat = personal_stat,top_posters = top_posters, worst_posts = worst_posts,best_posts = best_posts )

@app.route("/forms", methods = ['POST', 'GET'])
def forms_post():

    content = None
    title = None

    if request.method == 'POST' and "title" in request.form:
        title = request.form['title']

    if request.method == 'POST' and "content" in request.form:
        content = request.form['content']

    search = request.form['search_form']

    if title is None:# shorten
        if content is None:
            conn = sqlite3.connect("snowbaord.db")
            c = conn.cursor()
            c.execute("select * from formpost where post LIKE '%"+ search +"%' or title like '%"+ search +"%'")
            result = c.fetchall()
            conn.close()

    if title is None:# shorten
        if content is not None:
            conn = sqlite3.connect("snowbaord.db")
            c = conn.cursor()
            c.execute("select * from formpost where post LIKE '%"+ search +"%'")
            result = c.fetchall()
            conn.close()

    if title is not  None:# shorten
        if content is None:
            conn = sqlite3.connect("snowbaord.db")
            c = conn.cursor()
            c.execute("select * from formpost where title LIKE '%"+ search +"%'")
            result = c.fetchall()
            conn.close()

    if title is not None:# shorten
        if content is not None:
            conn = sqlite3.connect("snowbaord.db")
            c = conn.cursor()
            c.execute("select * from formpost where post LIKE '%"+ search +"%' or title like '%"+ search +"%'")
            result = c.fetchall()
            conn.close()

    conn = sqlite3.connect("snowbaord.db") # shorten
    c = conn.cursor()
    c.execute("select * from user where name =?",(session['username'],))
    personal_stat = c.fetchall()
    conn.close()


    return render_template('forms.html', user = session['username'], stat = personal_stat, result = result)

@app.route("/forms/create")
def forms_create():
    return render_template('create_post.html')


@app.route("/forms/create", methods = ['POST', 'GET'])
def forms_create_post():

    title = request.form['title']
    content = request.form['content']
    user = session["username"]
    time = datetime.datetime.now()

    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    sql = "INSERT INTO formpost (user, post, title, time) VALUES (?, ?, ?, ?)"
    val = (session['username'], content, title, time)
    c.execute(sql, val)
    conn.commit()
    conn.close()

    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    c.execute("select post from user where name =?",(session['username'],))
    amt = c.fetchall()
    b = amt[0][0]
    b += 1


    sql = "UPDATE user set post = "+ str(b) + " where name = "+ session["username"]+""
    c.execute(sql)
    conn.commit()

    conn.close()
    stat = b

    return render_template('create_post.html',stat = stat)

@app.route("/guide")
def guide():
    return render_template('guide.html')


if __name__ == "__main__":
    app.run(debug = True)
