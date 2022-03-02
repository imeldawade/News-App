from app import app
from flask import render_template

from .request import get_newss 

@app.route('/')
def index():

    items = get_newss('sources')

    title = 'Top Headlines'
    return render_template('index.html',title = title,sources=items)


