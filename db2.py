from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#from flask import render_template
#import os
#from sys import exc_info
#from flask import session

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

#class Conversion(db.Model):
#__table__='conversion'
#fahrenheit_unit = db.Column(db.Integer, db.ForeignKey('fahrenheit.f_id'))
#celsius_unit = db.Column(db.Integer, db.ForeignKey('celsius.c_id'))

conversion = db.Table('conversion',
db.Column('fahrenheit_unit',db.Integer, db.ForeignKey('fahrenheit.id')),
db.Column('celsius_unit', db.Integer, db.ForeignKey('celsius.id')),
db.Column('initial_val', db.Integer)
)

class Fahrenheit(db.Model):
    __tablename__='fahrenheit'
    id = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.Text)
    unit_conversion_divide = db.Column(db.Integer)
    unit_conversion_subtract = db.Column(db.Integer)
    celsius = db.relationship('Celsius', secondary = conversion, backref=db.backref('fahrenheits',lazy='dynamic'))


class Celsius(db.Model):
    __tablename__='celsius'
    id = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.Text)
    unit_conversion_multiply = db.Column(db.Integer)
    unit_conversion_add = db.Column(db.Integer)


db.drop_all()
db.create_all()
conversion1 = Celsius(id=1, unit_name='clss', unit_conversion_multiply = 1, unit_conversion_add = 32)
db.session.add(conversion1)
fahrenheit1 = Fahrenheit(id=2, unit_name='fhrnht', unit_conversion_divide = 1, unit_conversion_subtract = 32)
#kelvin1 = Kelvin(id=3, unit_name='k', unit_conversion_divide = 1, unit_conversion_subtract = 273.15)
db.session.add(fahrenheit1)

db.session.commit()
#@app.route('/')
#def initial_page():
# return "hello World"

#@app.route('/units')
#def subsequent_page():
# return render_template('layout.html')
