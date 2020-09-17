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


def filter( query):
    queryadd = ""
    if bcount >= 1: # if there is a brand entered
        if ccount == 1: # if there is only one color
                queryadd += "AND " # add filter
    if lcount > 0: # see if any color have already been put into the query
        if ccount > 1: # checking if there is more than one color
            queryadd += "OR " # add filter
    queryadd += query # add filter


    return(queryadd)







def filtersnowboots(Burton,DC,Small, Medium, Large,l200,l300,l400,l500,l600):

    bcount = 0 # counting how many brand request forms we have
    scount = 0 # counting how many size request forms we have
    pcount = 0 # counting how many price request forms we have


    brands = [Burton,DC]
    for i in range(len(brands)):
        if brands[i] is not None:
            bcount+= 1

    sizes = [Small, Medium, Large]
    for i in range(0,3):
        if sizes[i] is not None:
            scount+= 1

    prices = [l200,l300,l400,l500,l600]
    for i in range(0,4):
        if prices[i] is not None:
            pcount+= 1

    print(scount)
    print(pcount)
    print(bcount)

    allcount = bcount + scount + pcount

    fcount = 0 # using this to see how many brands have been placed in the query

    query = "SELECT * FROM snow_boots "

    if allcount > 0:
            query += "WHERE "

    if allcount > 0:
        query += "(" # if there is more than one brand to be filtered

    brand = ["'Burton'","'DC'"]

    for i in range(0,2):
        if brands[i] is not None:
            query += filterbrand(fcount, allcount, "brand = " + brand[i] +"")
            fcount += 1

    if bcount > 0 :
        query += ")"


    if bcount  > 0: # checking if and is neccessary and brackets
            if scount > 0:
                query += "AND ("

    if bcount == 0:
        if scount > 0:
            query+= "("

    gcount = 0

    size = ["'Small'","'Medium'","'Large'"]

    for i in range(0,3):
        if sizes[i] is not None:
            query += filtersize_noc(bcount, scount, gcount, "size = " + size[i] +"")
            gcount += 1

    if scount > 0:
        query += ")"

    kcount = 0 # counting if there has been a query
    if pcount > 0:
        if bcount or scount > 0:
            query += " AND "


    if  l600  is None:
        if l500 is not None:
            if kcount == 0:
                query += "price <= 500"
                kcount += 1

    if  l600 or l500  is None:
        if l400 is not None:
            if kcount ==0:
                query += "price <= 400"
                kcount += 1


    if  l600 or l500 or l400 is None:
        if l300 is not None:
            if kcount == 0:
                query += "price <= 300"
                kcount += 1

    if  l600 or l500 or l400 or l300 is None:
        if l200 is not None:
            if kcount == 0:
                query += "price <= 200"
                kcount += 1
    print(query)
    return(query)






















def filterclothes(Burton,North_Face,Macpac,Swandry,Kathmandu,Small, Medium, Large,\
l200,l300,l400,l500,l600):

    bcount = 0 # counting how many brand request forms we have
    scount = 0 # counting how many size request forms we have
    pcount = 0 # counting how many price request forms we have


    brands = [Burton,North_Face,Macpac,Swandry,Kathmandu]
    for i in range(0,5):
        if brands[i] is not None:
            bcount+= 1

    sizes = [Small, Medium, Large]
    for i in range(0,3):
        if sizes[i] is not None:
            scount+= 1

    prices = [l200,l300,l400,l500,l600]
    for i in range(0,4):
        if prices[i] is not None:
            pcount+= 1

    fcount = 0 # using this to see how many brands have been placed in the query

    query = "SELECT * FROM clothes "

    if bcount or scount or pcount > 0:
        if fcount == 0:
            query += "WHERE "

    if bcount > 0:
        query += "(" # if there is more than one brand to be filtered

    brand = ["'Burton'","'North_Face'","'Macpac'","'Swandry'","'Kathmandu'"]

    for i in range(0,5):
        if brands[i] is not None:
            query += filterbrand(fcount, bcount, "brand = " + brand[i] +"")
            fcount += 1

    if bcount > 0 :
        query += ")"


    if bcount  >= 1: # checking if and is neccessary and brackets
            if scount > 0:
                query += "AND ("

    gcount = 0

    size = ["'Small'","'Medium'","'Large'"]

    for i in range(0,3):
        if sizes[i] is not None:
            query += filtersize_noc(bcount, scount, gcount, "size = " + size[i] +"")
            gcount += 1

    print(query)


    if bcount >= 1:
        if scount >0:
            query += ")"

    kcount = 0 # counting if there has been a query
    if pcount > 0:
        if bcount or scount > 0:
            query += " AND "


    if  l600  is None:
        if l500 is not None:
            if kcount == 0:
                query += "price <= 500"
                kcount += 1

    if  l600 or l500  is None:
        if l400 is not None:
            if kcount ==0:
                query += "price <= 400"
                kcount += 1


    if  l600 or l500 or l400 is None:
        if l300 is not None:
            if kcount == 0:
                query += "price <= 300"
                kcount += 1

    if  l600 or l500 or l400 or l300 is None:
        if l200 is not None:
            if kcount == 0:
                query += "price <= 200"
                kcount += 1
    print(query)
    return(query)

















def filtersnowbinding(Jones_Snowboards,Gnu,Lib_Tech,Salomon,Burton,Small, Medium, Large,\
l200,l300,l400,l500,l600):

    bcount = 0 # counting how many brand request forms we have
    scount = 0 # counting how many size request forms we have
    pcount = 0 # counting how many price request forms we have


    brands = [Jones_Snowboards,Gnu,Lib_Tech,Salomon,Burton]
    for i in range(0,5):
        if brands[i] is not None:
            bcount+= 1

    sizes = [Small, Medium, Large]
    for i in range(0,3):
        if sizes[i] is not None:
            scount+= 1

    prices = [l200,l300,l400,l500,l600]
    for i in range(0,4):
        if prices[i] is not None:
            pcount+= 1

    fcount = 0 # using this to see how many brands have been placed in the query

    query = "SELECT * FROM snowbinding "

    if bcount or scount or pcount > 0:
        if fcount == 0:
            query += "WHERE "

    if bcount > 0:
        query += "(" # if there is more than one brand to be filtered

    brand = ["'Jones_Snowboards'", "'Gnu'", "'Lib_Tech'", "'Salomon'", "'Burton'"]

    for i in range(0,5):
        if brands[i] is not None:
            query += filterbrand(fcount, bcount, "brand = " + brand[i] +"")
            fcount += 1

    if bcount > 0 :
        query += ")"


    if bcount  >= 1: # checking if and is neccessary and brackets
            if scount > 0:
                query += "AND ("

    gcount = 0

    size = ["'Small'","'Medium'","'Large'"]

    for i in range(0,3):
        if sizes[i] is not None:
            query += filtersize_noc(bcount, scount, gcount, "size = " + size[i] +"")
            gcount += 1

    print(query)


    if bcount >= 1:
        if scount >0:
            query += ")"

    kcount = 0 # counting if there has been a query
    if pcount > 0:
        if bcount or scount > 0:
            query += " AND "


    if  l600  is None:
        if l500 is not None:
            if kcount == 0:
                query += "price <= 500"
                kcount += 1

    if  l600 or l500  is None:
        if l400 is not None:
            if kcount ==0:
                query += "price <= 400"
                kcount += 1


    if  l600 or l500 or l400 is None:
        if l300 is not None:
            if kcount == 0:
                query += "price <= 300"
                kcount += 1

    if  l600 or l500 or l400 or l300 is None:
        if l200 is not None:
            if kcount == 0:
                query += "price <= 200"
                kcount += 1

    return(query)































# snowbaord filterr r wwawf

def filtersnowbaord(Burton,Salomon,Lib_Tech,Jones_Snowboards,Gnu,blue,red,\
orange,pink,white,black,yellow,other,one_forty,one_forty_two,one_forty_four,\
one_forty_six,one_forty_eight,l200,l300,l400,l500,l600,g600):

    bcount = 0 # counting how many brand request forms we have
    ccount = 0 # counting how many color request forms we have
    scount = 0 # counting how many size request forms we have
    pcount = 0 # counting how many price request forms we have

    brands = [Jones_Snowboards,Gnu,Lib_Tech,Salomon,Burton]
    for i in range(0,5):
        if brands[i] is not None:
            bcount+= 1


    colors = [blue,orange,red,pink,white,black,yellow,other]
    for i in range(0,6):
        if colors[i] is not None:
            ccount+= 1

    sizes = [one_forty,one_forty_two,one_forty_four,one_forty_six,one_forty_eight]
    for i in range(0,5):
        if sizes[i] is not None:
            scount+= 1

    prices = [l200,l300,l400,l500,l600]
    for i in range(0,4):
        if prices[i] is not None:
            pcount+= 1

    print(bcount)
    print(ccount)
    print(scount)
    print(pcount)

    # braqndssssssssssssssssssssssssssssssss

    fcount = 0 # using this to see how many brands have been placed in the query

    query = "SELECT * FROM snowbaord "

    if bcount or ccount or scount or pcount > 0:
        if fcount == 0:
            query += "WHERE "

    if bcount > 0:
        query += "(" # if there is more than one brand to be filtered

    brand = ["'Jones_Snowboards'", "'Gnu'", "'Lib_Tech'", "'Salomon'", "'Burton'"]

    for i in range(0,5):
        if brands[i] is not None:
            query += filterbrand(fcount, bcount, "brand = " + brand[i] +"")
            fcount += 1

    if bcount > 0 :
        query += ")"

    # colorsssssssssssssssssssssss

    lcount = 0 # counting how many color have been put into the query

    if bcount >= 1:
        if ccount > 1:
            query += "AND (" #checks if there has been a brand and if there is more than one color

    if bcount == 0:
        if ccount >1:
            query += "(" # if no brand but more that one color



    if yellow is not None:
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


    # sizesssssssssssssssssssssssssssssssss
    gcount = 0

    if bcount or ccount >= 1: # checking if and is neccessary and brackets
            if scount > 1:
                query += "AND ("

    size = ["'140'","'142'","'144'","'146'","'148'"]

    for i in range(0,5):
        if sizes[i] is not None:
            query += filtersize(bcount, ccount, scount, gcount, "size = " + size[i] +"")
            gcount += 1



    if bcount or ccount >= 1:
        if scount >1:
            query += ")"

    # price

    kcount = 0 # counting if there has been a query
    if pcount > 0:
        if bcount or ccount or scount > 0:
            query += " AND "

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



    return(query)
