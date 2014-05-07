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
	#kelvin = db.relationship('Kelvin', secondary = conversion)
	#def __init__(self, id, unit_name, unit_conversion_divide, unit_conversion_subtract):
	#	self.id = id
	#	self.unit_name = unit_name
	#	self.unit_conversion_divide = unit_conversion_divide
	#	self.unit_conversion_subtract = unit_conversion_subtract

class Celsius(db.Model):
	__tablename__='celsius'
	id = db.Column(db.Integer, primary_key=True)
	unit_name = db.Column(db.Text)
	unit_conversion_multiply = db.Column(db.Integer) 
	unit_conversion_add = db.Column(db.Integer)
	#fahrenheit = db.relationship('Fahrenheit', secondary = conversion)
	#def __init__(self, id, unit_name, unit_conversion_multiply, unit_conversion_add):
	#	self.id = id
	#	self.unit_name = unit_name
	#	self.unit_conversion_multiply = unit_conversion_multiply
	#	self.unit_conversion_add = unit_conversion_add

	#kelvin = db.relationship('Kelvin', secondary = conversion)

#class Kelvin(db.Model):
	#__tablename__='kelvin'
	#k_id= db.Column(db.Integer, primary_key=True)
	#unit_name= db.Column(db.Text)
	#unit_conversion_add = (db.Float)
	#unit_conversion_multiply = (db.Integer)
	#celsius = db.relationship('Celsius', secondary= conversion)
	#fahrenheit= db.relationship('Fahrenheit', secondary = conversion)

db.drop_all()
db.create_all()
conversion1 = Celsius(id=1, unit_name='clss', unit_conversion_multiply = 1.8, unit_conversion_add = 32)
db.session.add([conversion1])
fahrenheit1 = Fahrenheit(id=2, unit_name='fhrnht', unit_conversion_divide = 0.56, unit_conversion_subtract = 32)
#kelvin1 = Kelvin(id=3, unit_name='k', unit_conversion_divide = 1, unit_conversion_subtract = 273.15)
db.session.add([fahrenheit1])

db.session.commit()
#@app.route('/')
#def initial_page():
#	return "hello World"

#@app.route('/units')
#def subsequent_page():
#	return render_template('layout.html')
