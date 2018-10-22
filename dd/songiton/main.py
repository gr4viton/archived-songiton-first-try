#-*-coding:utf8;-*-
#qpy:3
#qpy:webapp:Sample 
#qpy://localhost:8080/
"""
This is a sample for qpython webapp
"""

from flask import Flask 

app = Flask(__name__)

@app.route('/') 
def hello_world(): 
     return 'Hello, World!'

# from bottle import route, run

# @route('/')
# def hello():
#     return "Hello World!"

# run(host='localhost', port=8080)

