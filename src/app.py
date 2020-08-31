import os
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy



# Init App
budget_app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#SQLAlchemy databse 
budget_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db')
budget_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init Database
db = SQLAlchemy(budget_app)

# Init Marshmallow
ma = Marshmallow(budget_app)

# Budget Class/Model
class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    amount = db.Column(db.Float)

    def __init__(self, name, description, amount):
        self.name = name
        self.description = description
        self.amount = amount

# Budget Schema
class BudgetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'amount')

# Init schema
budget_schema = BudgetSchema()
budgets_schema = BudgetSchema(many=True)

# Create a Budget
@budget_app.route('/budget', methods=['POST'])
def add_budget():
    name = request.json['name']
    description = request.json['description']
    amount = request.json['amount']


    new_budget = Budget(name, description, amount)
    db.session.add(new_budget)
    db.session.commit()

    return budget_schema.jsonify(new_budget)


# To Run Server
if __name__ == '__main__':
    budget_app.run(debug=True)
    