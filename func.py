from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3

def database(query):

    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    c.execute(query)
    result = c.fetchall()
    conn.close()
    return (result)

def filterbrand(fcount, bcount, query):
    queryadd = ""
    if fcount > 0:# checking whether another brand has be input into the query
        if bcount == 1: # if there is only one brand
            queryadd += "AND " # add filter
    if fcount > 0: # checking if another brand is in query
        if bcount >1: # checking if another brand is in query
            queryadd += "OR " # if another brand has been entered
    queryadd += query # Add Filter

    return(queryadd)

def filtercolor(lcount, bcount, ccount, query):
    queryadd = ""
    if bcount >= 1: # if there is a brand entered
        if ccount == 1: # if there is only one color
                queryadd += "AND " # add filter
    if lcount > 0: # see if any color have already been put into the query
        if ccount > 1: # checking if there is more than one color
            queryadd += "OR " # add filter
    queryadd += query # add filter


    return(queryadd)

def filtersize(bcount, ccount, scount, gcount, query) :
    queryadd = ""
    if bcount or ccount >= 1:
        if scount == 1: # seeing if and is neccary with no brakets
            queryadd  += " AND " # Add Filter
    if gcount > 0: # if more than one size has been added to the query
        if scount > 1: # checking if ther has been more than filter for size
            queryadd  += "OR " # Add Filter
    queryadd  += query # Add Filter

    return(queryadd)
    
def filtersnowbaord(Burton,Salomon,Lib_Tech,Jones_Snowboards,Gnu,blue,red,\
orange,pink,white,black,yellow,other,one_forty,one_forty_two,one_forty_four,\
one_forty_six,one_forty_eight,l200,l300,l400,l500,l600,g600):

    bcount = 0 # counting how many brand request forms we have
    ccount = 0 # counting how many color request forms we have
    scount = 0 # counting how many size request forms we have
    pcount = 0 # counting how many price request forms we have

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

    lcount = 0 # counting how many color have been put into the query

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

    conn = sqlite3.connect('snowbaord.db')# shorten
    c = conn.cursor()
    c.execute(query)
    test = c.fetchall()
    conn.close()


    return(query)
