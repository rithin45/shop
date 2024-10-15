from flask import Flask,Blueprint,render_template

from database import *

shop=Blueprint('shop',__name__)

@shop.route('/shop_home')
def shop_home():
    return render_template('shop_home.html')