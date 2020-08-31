import os
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy



# Init App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#SQLAlchemy databse 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init Database
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)

# To Run Server
if __name__ == '__main__':
    app.run(debug=True)
    
