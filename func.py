from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3

def database(query):

    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    c.execute(query)
    result = c.fetchall()
    conn.close()
    return (result)

def database_var(query, var): # dtabase with variable

    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    c.execute(query,var)
    result = c.fetchall()
    conn.close()
    return (result)



def filter(brands, sizes, size_ids,):

    size_id = {

    }


    for i in range(len(size_ids)):
        for p in range (0,1):
            size_id[size_ids[i][1]] = size_ids[i][p]

    #sorting into either a brand or size
    type = {

    }


    for brand in brands:
        type[brand[0]] = "1"

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

    # giving all of the items keys
    keys = {

    }

    for f in range(len(filter_options)):
        keys[f] = filter_options[f]

    return(size_id, filters, filter_options, type, keys)


def filter_post(queries, keys, type, filter_options, filters, size_id, query):

    bcount = 0  #amount of brands
    scount = 0  # amount of sizes
    icount = 0  # how many itmes overall

    items_to_filter = []

    for i in range(len(filter_options)):

        item = request.form.get(filter_options[i])
        if item is not None:
            items_to_filter.append(i)
            icount += 1

    # seeing if there is anything to be sorted
    if icount > 0:
        ##counting how many brands and sizes
        for i in range(len(items_to_filter)):
            fil = str(items_to_filter[i])
            item = keys[fil]
            if type[item] == '1':
                bcount += 1
            else:
                scount += 1
        #counting how many times something has bee added
        pcount = 0
        fcount = 0

        if len(items_to_filter) > 0:
            query += "where "

        if bcount > 0:
            query += "("

        for i in range(len(items_to_filter)):
            a = keys[str(items_to_filter[i])]
            a = str(a)
            if type[a] == "1":
                if i >= 1:
                    query += "or "
                    query += queries["1"]
                    query += "'"  + keys[str(items_to_filter[i])] + "'"
                else:
                    query += queries["1"]
                    query += "'"  + keys[str(items_to_filter[i])] + "' "

            if type[a] == "2":

                if bcount > 0 and fcount == 0:
                    query += ") and ( "
                    fcount += 1

                elif scount > 0 and bcount == 0 and fcount == 0:
                    query += "("
                    fcount += 1

                if pcount >= 1:
                    query += "or "
                    query += queries["2"]
                    a = keys[str(items_to_filter[i])]
                    b = size_id[a]
                    query += str(b) + ")"
                    pcount +=1
                else:
                    query += queries["2"]
                    a = keys[str(items_to_filter[i])]
                    b = size_id[a]
                    query += str(b) + ")"
                    pcount +=1

        if scount > 0 or bcount > 0:
            query += ")"
    return(query)
