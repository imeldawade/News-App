from app import app
from flask import render_template

from .request import get_newss

@app.route('/')
def index():

    popular_newss = get_newss
    print(popular_newss)
    title = 'Home - Top Headlines'
    return render_template('index.html', title = title,popular = popular_newss)

    
