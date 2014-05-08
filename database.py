from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy.types as types
from flask import render_template
#import os
#from sys import exc_info
#from flask import session

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
db = SQLAlchemy(app)

conversion = db.Table('conversion',
	db.Column('fahrenheit_unit',db.Integer, db.ForeignKey('fahrenheit.id')),
	db.Column('celsius_unit', db.Integer, db.ForeignKey('celsius.id')),
	db.Column('kelvin_unit', db.Integer, db.ForeignKey('kelvin.id'))
	#db.Column('initial_val', db.Integer)
)

class Fahrenheit(db.Model):
	__tablename__='fahrenheit'
	id = db.Column(db.Integer, primary_key=True)
	unit_name = db.Column(db.Text)
	unit_conversion_divide = db.Column(db.Float)
	unit_conversion_subtract = db.Column(db.Integer)
	celsius = db.relationship('Celsius', secondary = conversion)
	kelvin = db.relationship('Kelvin', secondary = conversion)

class Celsius(db.Model):
	__tablename__='celsius'
	id = db.Column(db.Integer, primary_key=True)
	unit_name = db.Column(db.Text)
	unit_conversion_multiply = db.Column(db.Float) 
	unit_conversion_add = db.Column(db.Integer)
	fahrenheit = db.relationship('Fahrenheit', secondary = conversion)
	kelvin = db.relationship('Kelvin', secondary = conversion)

class Kelvin(db.Model):
	__tablename__='kelvin'
	id= db.Column(db.Integer, primary_key=True)
	unit_name= db.Column(db.Text)
	unit_conversion_num = db.Column(db.Float)
	unit_conversion_frac = db.Column(db.Float)
	celsius = db.relationship('Celsius', secondary= conversion)
	fahrenheit= db.relationship('Fahrenheit', secondary = conversion)

class Custom_Unit(db.Model):
	__tabename__='custom_unit'
	id=db.Column(db.Integer, primary_key=True)
	custom_unit_name = db.Column(db.String(30))

	def __init__(self, custom_unit_name):
		self.custom_unit_name

class Custom_Convert(db.Model):
	__tabename__ = 'custom_unit_convert'
	id = db.Column(db.Integer, primary_key=True)
	custom_convert = db.Column(db.String(30))

	def __init__(self, custom_convert):
		self.custom_convert = custom_convert

def unit_validation(custom_unit_name):
	"""validate unit name using regular expression to make sure it doesn't contain any of theses characters"""
	if re.match("[@!#$%^&*()0-9*+=~`\-/><;:\[\]\]+"):
		return False
	return True


db.drop_all()
db.create_all()
celsius_to_fahrenheit = Celsius(id=1, unit_name='c_to_f', unit_conversion_multiply = 1.8, unit_conversion_add = 32)
db.session.add(celsius_to_fahrenheit)
fahrenheit_to_celsius = Fahrenheit(id=2, unit_name='f_to_c', unit_conversion_divide = 0.56, unit_conversion_subtract = 32)
kelvin_to_celsius = Kelvin(id=3, unit_name='k_to_c', unit_conversion_frac = 1.0, unit_conversion_num = 273.15)
kelvin_to_fahrenheit = Kelvin(id=4, unit_name='k_to_f', unit_conversion_frac = 1.8, unit_conversion_num = 459.67)
fahrenheit_to_kelvin = Kelvin(id=5, unit_name='f_to_k', unit_conversion_frac = 0.56, unit_conversion_num = 459.67)

db.session.add_all([fahrenheit_to_celsius, kelvin_to_fahrenheit, kelvin_to_celsius, fahrenheit_to_kelvin])

db.session.commit()

#this part will be moved to the controller file
@app.route('/')
def initial_page():
	return "Units Conversion CS365 Final Project."

@app.route('/units')
def subsequent_page():
	return render_template('layout.html')

if __name__ == '__main__':
	app.run(debug=True)

	 
