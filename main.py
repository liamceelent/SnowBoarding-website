from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3
from func import database, database_var, filter, filter_post
import os
import hashlib


app = Flask(__name__)

app.config['SECRET_KEY'] = 'super secret key'
app.config['SESSION_PERMANENT'] = False

@app.route("/")
def home():
    if "username" in session:
        loggedstat = "you are logged in as", session['username']
        return render_template('home.html', loggedstat = loggedstat) #home page if logged in
    else:
        session['username'] = "guest"
        return render_template('home.html') #home page if not logged in

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/login", methods = ['POST'])
def create_acc():

    if request.method == 'POST' and "logout" in request.form:
        session['username'] = "guest"
        return redirect(url_for("home"))

    if request.method == 'POST' and "create_name" in request.form: # seeing if account has been maid

        name = request.form['create_name']
        password = request.form['create_pass']

        names = database("select name from user") # ask sir about this

        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

        conn = sqlite3.connect("snowbaord.db")
        brand = []
        brand.insert(0, name)
        brand.insert(1, salt)
        brand.insert(2, key)
        brand = tuple(brand)

        query = "INSERT INTO user(name, salt, key) VALUES(?, ?, ?)" # inserting an account

        c = conn.cursor()
        c.execute(query, brand)
        conn.commit()
        conn.close() # creating a account
        stat = "account created"
        return render_template('login.html', stat = stat)

    if request.method == 'POST' and "name" in request.form: # checking if login maths

        name = request.form['name']
        password = request.form['pass']

        conn = sqlite3.connect("snowbaord.db")
        c = conn.cursor()
        c.execute("select salt, key from user where name = ?",(name,))
        result = c.fetchall() # retreiving password and username for login
        conn.close()

        if not result:
            stat = "wrong user name mate"
            return render_template('login.html', stat=stat)
        else:
            salt = result[0][0]
            key = result[0][1]
            new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
            if key == new_key: # seeing if they match
                session["username"] = name # setting sesion username
                return redirect(url_for("home"))
            else:
                stat = "wrong user name mate"
                return render_template('login.html', stat=stat)


    return render_template('login.html')


@app.route("/gear", methods = ['POST', 'GET']) # gear page
def gear_page():

    return render_template('gear.html')



@app.route("/gear_snowbinding")
def gear_snowbinding():

    brands = database("select name from snowbinding_brands")

    sizes = database("select size from size")

    size_ids = database("select id, size from size")

    results = filter(brands,sizes,size_ids)

    size_id = results[0]
    filters = results[1]
    filter_options = results[2]
    type = results[3]
    keys = results[4]

    # sending all variables over to post
    session['keys'] = keys
    session['type'] = type
    session['filter_options'] = filter_options
    session['filters'] = filters
    session['size_id'] = size_id

    return render_template('gear_snowbinding.html', filter_options = filter_options, filter = filters,key = keys)


@app.route("/gear_snowbinding", methods = ['POST', 'GET'])
def gear_snowbinding_post():

    queries = {

    "1": "brand = ",
    "2": "id in (select snowbinding_id from snowbinding_size where size_id = "

    }
    # getting al variables
    keys = session.get('keys')

    type = session.get('type')

    filter_options = session.get('filter_options')

    filters = session.get('filters')

    size_id = session.get('size_id')

    query_start = "select * from snowbinding "


    query = filter_post(queries,keys,type,filter_options,filters,size_id,query_start)

    print(query)

    conn = sqlite3.connect('snowbaord.db')
    c = conn.cursor()
    c.execute(query)
    query_r = c.fetchall()
    conn.close()

    if request.method == 'POST' and "search_bar" in request.form:
        search_clothes = request.form['search_bar']
        query_r  = database("select * from clothes where name LIKE '%"+ search_clothes +"%'")

    return render_template('gear_snowbinding.html', snowbinding_r = query_r, filter_options = filter_options,filter = filters,key = keys)

@app.route("/gear_snowbaord")
def gear_snowbaord():

    brands = database("select name from snowbaord_brands")

    sizes = database("select size from size")

    size_ids = database("select id, size from size")

    results = filter(brands,sizes,size_ids)

    size_id = results[0]
    filters = results[1]
    filter_options = results[2]
    type = results[3]
    keys = results[4]

    # sending all variables over to post
    session['keys'] = keys
    session['type'] = type
    session['filter_options'] = filter_options
    session['filters'] = filters
    session['size_id'] = size_id

    return render_template('gear_snowbaord.html', filter_options = filter_options, filter = filters,key = keys)

@app.route("/gear_snowbaord", methods = ['POST', 'GET'])
def gear_snowbaord_post():

    queries = {

    "1": "brand = ",
    "2": "id in (select snowbaord_id from snowbaord_size where size_id = "

    }
    # getting al variables
    keys = session.get('keys')

    type = session.get('type')

    filter_options = session.get('filter_options')

    filters = session.get('filters')

    size_id = session.get('size_id')

    query_start = "select * from snowbaord "


    query = filter_post(queries,keys,type,filter_options,filters,size_id,query_start)

    print(query)

    conn = sqlite3.connect('snowbaord.db')
    c = conn.cursor()
    c.execute(query)
    query_r = c.fetchall()
    conn.close()

    if request.method == 'POST' and "search_bar" in request.form:
        search_clothes = request.form['search_bar']
        query_r  = database("select * from clothes where name LIKE '%"+ search_clothes +"%'")

    return render_template('gear_snowbaord.html', snowboard_r = query_r, filter_options = filter_options,filter = filters,key = keys)

@app.route("/gear_clothes")
def gear_clothes():

    brands = database("select name from clothes_brands")

    sizes = database("select size from size")

    size_ids = database("select id, size from size")

    results = filter(brands,sizes,size_ids)

    size_id = results[0]
    filters = results[1]
    filter_options = results[2]
    type = results[3]
    keys = results[4]

    # sending all variables over to post
    session['keys'] = keys
    session['type'] = type
    session['filter_options'] = filter_options
    session['filters'] = filters
    session['size_id'] = size_id

    return render_template('gear_clothes.html', filter_options = filter_options, filter = filters,key = keys)




@app.route("/gear_clothes", methods = ['POST'])
def gear_clothes_post():

    queries = {

    "1": "brand = ",
    "2": "id in (select clothes_id from clothes_size where size_id = "

    }
    # getting al variables
    keys = session.get('keys')

    type = session.get('type')

    filter_options = session.get('filter_options')

    filters = session.get('filters')

    size_id = session.get('size_id')

    query_start = "select * from clothes "


    query = filter_post(queries,keys,type,filter_options,filters,size_id,query_start)

    print(query)
    print(keys)

    conn = sqlite3.connect('snowbaord.db')
    c = conn.cursor()
    c.execute(query)
    query_r = c.fetchall()
    conn.close()

    if request.method == 'POST' and "search_bar" in request.form:
        search_clothes = request.form['search_bar']
        query_r  = database("select * from clothes where name LIKE '%"+ search_clothes +"%'")

    return render_template('gear_clothes.html', clothes_r = query_r, filter_options = filter_options,filter = filters,key = keys)

@app.route("/gear_snow_boots")
def gear_snow_boots():
     # getting all the things to filter by

    brands = database("select name from snowboots_brands")

    sizes = database("select size from size")

    size_ids = database("select id,size from size")

    # getting the size id from database

    results = filter(brands,sizes,size_ids)

    size_id = results[0]
    filters = results[1]
    filter_options = results[2]
    type = results[3]
    keys = results[4]

    # sending all variables over to post
    session['keys'] = keys
    session['type'] = type
    session['filter_options'] = filter_options
    session['filters'] = filters
    session['size_id'] = size_id

    return render_template('gear_snow_boots.html', filter_options = filter_options, filter = filters,key = keys)

@app.route("/gear_snow_boots", methods = ['POST'])
def gear_snow_boots_post():

    # queries between brands and sizes
    queries = {

    "1": "brand = ",
    "2": "id in (select snowboot_id from snowboots_size where size_id = "

    }
    # getting al variables
    keys = session.get('keys')

    type = session.get('type')

    filter_options = session.get('filter_options')

    filters = session.get('filters')

    size_id = session.get('size_id')

    query_start = "select * from snowboots "


    query = filter_post(queries,keys,type,filter_options,filters,size_id,query_start)

    conn = sqlite3.connect('snowbaord.db')
    c = conn.cursor()
    c.execute(query)
    query_r = c.fetchall()
    conn.close()

    if request.method == 'POST' and "search_bar" in request.form:
        search_snowboots = request.form['search_bar']
        query_r = database("select * from snowboots where name LIKE '%"+ search_snowboots +"%'")

    print(query_r)
    return render_template('gear_snow_boots.html', snowboots_r = query_r, filter_options = filter_options,filter = filters,key = keys)


@app.route("/gear_click")
def gear_click():

    search_id = request.args.get('search_id')
    table = request.args.get('table')

    if table == "3":
        result = database_var("select * from snowbaord where id = ?",(search_id,)) # indivudual gear click for snowbaord

    if table == "4":
        result = database_var("select * from snowbinding where id = ?",(search_id,)) # " " " "


    if table == "2":
        result = database_var("select * from snowboots where id = ?",(search_id,)) # " " " "


    if table == "1":
        result = database_var("select * from clothes where id = ?",(search_id,)) # " " " " clothes


    return render_template('gearspec.html', name = search_id, result = result, table= table)





@app.route("/forms")
def forms():

    all_forms = database("select * from formpost")

    personal_stat = database_var("select * from user where name =?",(session['username'],))

    return render_template('forms.html', all_forms = all_forms, stat = personal_stat)

@app.route("/forms", methods = ['POST', 'GET'])
def forms_post():
    content = None
    title = None

    if request.method == 'POST' and "title" in request.form:
        title = request.form['title']

    if request.method == 'POST' and "content" in request.form:
        content = request.form['content']

    if request.method == 'POST' and "search_form" in request.form:
        search = request.form['search_form']

    if title is None:
        if content is None: # plain searching
            result = database("select * from formpost where title LIKE '%"+ search +"%' OR post LIKE '%"+ search +"%'")

    if title is None:
        if content is not None: # searching content
            result = database("select * from formpost where post LIKE '%"+ search +"%'")

    if title is not  None: # searching title
        if content is None:
            result = database("select * from formpost where title LIKE '%"+ search +"%'")

    if title is not None:
        if content is not None: #searching both content and title
            result = database("select * from formpost where title LIKE '%"+ search +"%' OR post LIKE '%"+ search +"%'")

    personal_stat = database_var("select * from user where name =?",(session['username'],))


    return render_template('forms.html', user = session['username'], stat = personal_stat, all_forms = result)

@app.route("/forms/create")
def forms_create():
    if session['username'] != "guest": #see if logged in
        return render_template('create_post.html')
    else:
        stat = "please login"
        return redirect(url_for("login"))


@app.route("/forms/create", methods = ['POST', 'GET'])
def forms_create_post():
    title = request.form['title']
    content = request.form['content']
    user = session["username"]


    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    sql = "INSERT INTO formpost (user, post, title) VALUES (?, ?, ?)"
    val = (session['username'], content, title)
    c.execute(sql, val)
    conn.commit()


    conn.close()
    stat = "post made :)"

    return render_template('create_post.html',stat = stat)

@app.route("/guide")
def guide():
    return render_template('guide.html')


if __name__ == "__main__":
    app.run(debug = True)
