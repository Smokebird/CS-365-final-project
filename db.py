from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy.types as types

app = Flask(__name__)
app.config['AQLALCHEMY_DATABASE_URI'] = 'sqlite:////temp/test.db'
db = SQLAlchemy(app)

#class EqType(types.TypeDecorator):
 #   impl = types.Interger

#class Temp(db.Model):
 #   __tablename__ = 'course'
    
class Fahrenheit(db.Model):
    __tablename__='fahrenheit'
    f_id = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.Text)
    unit_conversion_divide = (db.Float)
    unit_conversion_subtract = (db.Integer)

db.drop_all
db.create_all()
fahrenheit1 = Fahrenheit(f_id=2, unit_name='fhrnht', unit_conversion_divide = 0.56, unit_conversion_subtract = 32)
db.session.add_all([fahrenheit1])

@app.route('/')
def initial_page():
    return "hello World"

@app.route('/units')
def subsequent_page():
     return render_template('layout.html')


if __name__=='__main__':
    app.run()
