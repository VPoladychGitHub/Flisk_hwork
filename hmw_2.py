import os
from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route('/requirements')
def requirements():
    f = open('requirements.txt', 'r')
    s: str = ''
    for line in f.readlines():
        s = s + str(line) + '\n'
    f.close()
    return s

# python -m flask run