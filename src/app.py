#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import os

app = Flask(__name__)

posts = [
    {
        'author': 'Maros Kukan',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'June 23, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'June 24, 2021'
    }
]

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)