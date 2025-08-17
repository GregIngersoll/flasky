from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Greg Ingersoll'}
    posts = [
        {
            'author' : {'username':'Bob'},
            'body' : 'Bob''s book'
        },
        {
            'author' : {'username' : 'Sally' },
            'body' : 'Sally''s book'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
