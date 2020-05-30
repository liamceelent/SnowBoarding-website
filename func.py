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
