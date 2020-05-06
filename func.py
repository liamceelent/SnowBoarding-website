from flask import Flask, redirect, url_for, render_template, request, session
import sqlite3

def database(query):

    conn = sqlite3.connect("snowbaord.db")
    c = conn.cursor()
    c.execute(query)
    result = c.fetchall()
    conn.close()
    return (result)
