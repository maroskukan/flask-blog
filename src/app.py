#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return '<h1>Home Page</h1>'


@app.route('/about')
def about():
    return '<h1>About Page</h1>'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)