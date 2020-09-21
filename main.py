from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3
from func import database, filtersnowbaord, database_var, filtersnowbinding,filterclothes,filtersnowboots
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



@app.route("/gear_snowbinding", methods = ['POST', 'GET'])
def gear_snowbinding():
    search_snowbinding = request.form.get('search_bar')

    #brands request
    Burton = request.form.get('Burton')
    Salomon = request.form.get('Salomon')
    Lib_Tech = request.form.get('Lib_Tech')
    Jones_Snowboards = request.form.get('Jones_Snowboards')
    Gnu = request.form.get('Gnu')
    # sizes "

    Large = request.form.get('Large')
    Medium = request.form.get('Medium')
    Small = request.form.get('Small')

    #prices "

    l200 = request.form.get('200')
    l300 = request.form.get('300')
    l400 = request.form.get('400')
    l500 = request.form.get('500')
    l600 = request.form.get('600')

    snowbinding_r = database("select * from snowbinding where id >= 1") # r stands for result

    if search_snowbinding is not None:
        search_snowbinding = database("select * from snowbinding where name LIKE '%"+ search_snowbinding +"%'")
        return render_template('gear_snowbinding.html', snowbinding_r = search_snowbinding)

    query = filtersnowbinding(Jones_Snowboards,Gnu,Lib_Tech,Salomon,Burton,Small, Medium, Large,\
    l200,l300,l400,l500,l600) #func filter

    conn = sqlite3.connect('snowbaord.db')
    c = conn.cursor()
    c.execute(query)
    query_r = c.fetchall()
    conn.close()

    return render_template('gear_snowbinding.html', snowbinding_r = query_r) # page load without search






@app.route("/gear_snowbaord", methods = ['POST', 'GET'])
def gear_snowbaord():

    search_snowboard = request.form.get('search_bar')

    #brands request

    Burton = request.form.get('Burton')
    Salomon = request.form.get('Salomon')
    Lib_Tech = request.form.get('Lib_Tech')
    Jones_Snowboards = request.form.get('Jones_Snowboards')
    Gnu = request.form.get('Gnu')

    #colour "
    blue = request.form.get('blue')
    red = request.form.get('red')
    orange = request.form.get('orange')
    pink = request.form.get('pink')
    white = request.form.get('white')
    black = request.form.get('black')
    yellow = request.form.get('yellow')
    other = request.form.get('other')
    green = request.form.get('green')

    # sizes "

    one_forty = request.form.get('140')
    one_forty_two = request.form.get('142')
    one_forty_four = request.form.get('144')
    one_forty_six = request.form.get('146')
    one_forty_eight = request.form.get('148')

    #prices "

    l200 = request.form.get('200')
    l300 = request.form.get('300')
    l400 = request.form.get('400')
    l500 = request.form.get('500')
    l600 = request.form.get('600')
    g600 = request.form.get('600+')

    # search bar code
    if search_snowboard is not None:
        search_snowboard_r = database("select * from snowbaord where name LIKE '%"+ search_snowboard +"%'")
        return render_template('gear_snowbaord.html', search_snowboard_r = search_snowboard_r)

    query = filtersnowbaord(Burton,Salomon,Lib_Tech,Jones_Snowboards,Gnu,blue,red,\
    orange,pink,white,black,yellow,other,one_forty,one_forty_two,one_forty_four,\
    one_forty_six,one_forty_eight,l200,l300,l400,l500,l600,g600) #func filter

    conn = sqlite3.connect('snowbaord.db')
    c = conn.cursor()
    c.execute(query)
    query_r = c.fetchall()
    conn.close()

    return render_template("gear_snowbaord.html", search_snowboard_r = query_r)


@app.route("/gear_clothes", methods = ['POST', 'GET'])
def gear_clothes():

    Burton = request.form.get('Burton')
    North_Face = request.form.get('North_Face')
    Macpac = request.form.get('Macpac')
    Swandry = request.form.get('Swandry')
    Kathmandu = request.form.get('Kathmandu')

    # sizes "

    Large = request.form.get('Large')
    Medium = request.form.get('Medium')
    Small = request.form.get('Small')

    #prices "

    l200 = request.form.get('200')
    l300 = request.form.get('300')
    l400 = request.form.get('400')
    l500 = request.form.get('500')
    l600 = request.form.get('600')


    if request.method == 'POST' and "search_bar" in request.form:
        search_clothes = request.form['search_bar']
        search_clothes_r  = database("select * from clothes where name LIKE '%"+ search_clothes +"%'")
        return render_template('gear_clothes.html', clothes_r = search_clothes_r)

    query = filterclothes(Burton,North_Face,Macpac,Swandry,Kathmandu,Small, Medium, Large,\
    l200,l300,l400,l500,l600)

    conn = sqlite3.connect('snowbaord.db')
    c = conn.cursor()
    c.execute(query)
    query_r = c.fetchall()
    conn.close()

    return render_template('gear_clothes.html', clothes_r = query_r)

@app.route("/gear_snow_boots")
def gear_snow_boots():

    brands = database("select name from snowboots_brands")

    sizes = database("select size from size")

    type = {

    }


    for brand in brands:
        type[brand[0]] = "1"  # need to wrok on getting tpyes sorted

    for size in sizes:
        type[size[0]] = "2"

    filter_options = []

    for brand in brands:
        filter_options.append(brand[0])

    for size in sizes:
        filter_options.append(size[0])

    filters = []

    for i in range(len(filter_options)):
        filters.append(i)

    print(filters)
    print(filter_options)

    keys = {

    }

    for f in range(len(filter_options)):
        keys[f] = filter_options[f]

    print(keys)
    print(type)
    print(keys[0])

    session['keys'] = keys
    session['type'] = type
    session['filter_options'] = filter_options


    return render_template('gear_snow_boots.html', filter_options = filter_options, filter = filters,key = keys)

@app.route("/gear_snow_boots", methods = ['POST'])
def gear_snow_boots_post():

    queries = {

    "1": "brand =",
    "2": "SELECT * FROM snowboots WHERE id = (select snowboot_id from snowboots_size where size_id = )"

    }

    keys = session.get('keys')

    type = session.get('type')

    filter_options = session.get('filter_options')

    bcount = 0
    scount = 0

    items_to_filter = []

    print(filter_options)

    for i in range(len(filter_options)):

        item = request.form.get(filter_options[i])
        if item is not None:
            items_to_filter.append(i)

    fil = str(items_to_filter[0])

    print(items_to_filter)

    for i in range(len(items_to_filter)):
        fil = str(items_to_filter[i])
        item = keys[fil]
        if type[item] == '1':
            bcount += 1
        else:
            scount += 1

    query = "select * from snowboots "

    if len(items_to_filter) > 0:
        query += "where "

    if bcount > 0:
        query += "("
        
    if icount > 0:
        if bcount




    print(query)
    print(keys)
    print(type)
    print(bcount)
    print(scount)





    if request.method == 'POST' and "search_bar" in request.form:
        search_snowboots = request.form['search_bar']
        search_snowboots_r = database("select * from snow_boots where name LIKE '%"+ search_snowboots +"%'")
        return render_template('gear_snow_boots.html', snowboots_r = search_snowboots_r)

    conn = sqlite3.connect('snowbaord.db')
    c = conn.cursor()
    c.execute(query)
    query_r = c.fetchall()
    conn.close()

    return render_template('gear_snow_boots.html', snowboots_r = query_r)


@app.route("/gear_click")
def gear_click():

    search_id = request.args.get('search_id')
    table = request.args.get('table')

    if table == "3":
        result = database_var("select * from snowbaord where id = ?",(search_id,)) # indivudual gear click for snowbaord

    if table == "4":
        result = database_var("select * from snowbinding where id = ?",(search_id,)) # " " " "


    if table == "2":
        result = database_var("select * from snow_boots where id = ?",(search_id,)) # " " " "


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
    time = datetime.datetime.now()

    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    sql = "INSERT INTO formpost (user, post, title, time) VALUES (?, ?, ?)"
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
