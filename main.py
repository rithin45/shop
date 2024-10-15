from flask import Flask
from public import public
from admin import admin
from user import user
from shop import shop



app=Flask(__name__)
app.secret_key="thhhhhhh"



app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(user)
app.register_blueprint(shop)


app.run(debug=True)