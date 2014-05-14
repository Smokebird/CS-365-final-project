from flask import Flask, render_template, redirect, request, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy.types as types
from flask_wtf import Form
from wtforms import TextField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.debug = True
app.config['AQLALCHEMY_DATABASE_URI'] = 'sqlite:////temp/test.db'
db = SQLAlchemy(app)
app.secret_key = 'b\xdfp\xee-\xce\x9c\x15N]D\xb3\x01\x1f\x8a)!1x8x9\xc6R\x18y'
#class EqType(types.TypeDecorator):
 #   impl = types.Interger

#class Temp(db.Model):
 #   __tablename__ = 'course'




class MyForm(Form):
    number = TextField('number', validators = [DataRequired()])
    Conversion = SelectField('Conversion')
    Conversion2 = SelectMultipleField('Conversion2', choices=[('cpp', 'c++'),('py','Python')])
    Conversion3 = SelectMultipleField('Conversion3')

class TempForm(Form):
    Number = TextField('Number', validators=[DataRequired()])
    Con = SelectField('Conversion', validators=[DataRequired()])    
    

conversion = db.Table('conversion',
db.Column('fahrenheit_unit',db.Integer, db.ForeignKey('fahrenheit.f_id')),
db.Column('celsius_unit', db.Integer, db.ForeignKey('celsius.c_id')),
db.Column('initial_val', db.Integer)
)


class Fahrenheit(db.Model):
    __tablename__='fahrenheit'
    f_id = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.Text)
    unit_conversion_divide = (db.Float)
    unit_conversion_subtract = (db.Integer)
    celsius = db.relationship('Celsius' , secondary = conversion)


class Celsius(db.Model):
    __tablename__='celsius'
    c_id = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.Text)
    unit_conversion_multiply = (db.Float)
    unit_conversion_add = (db.Integer)
    fahrenheit = db.relationship('Fahrenheit', secondary = conversion)

class Kelvin(db.Model):
    __tablename__='kelvin'
    k_id= db.Column(db.Integer, primary_key=True)
    unit_name= db.Column(db.Text)
    unit_conversion_add = (db.Float)
    unit_conversion_multiply = (db.Integer)

class Custom_Unit(db.Model):
	__tabename__='custom_unit'
	id=db.Column(db.Integer, primary_key=True)
	custom_unit_name = db.Column(db.String(30))

	def __init__(self, custom_unit_name):
		self.custom_unit_name

	def unit_validation(custom_unit_name):
	"""validate unit name using regular expression to make sure it doesn't contain any of these characters"""
	if re.match("[@!#$%^&*()0-9*+=~`-/><;:[]]+"):
		return False
	return True


class Custom_Convert(db.Model):
	__tabename__ = 'custom_unit_convert'
	id = db.Column(db.Integer, primary_key=True)
	custom_convert = db.Column(db.String(30))

	def __init__(self, custom_convert):
		self.custom_convert = custom_convert

def unit_validation(custom_unit_name):
	"""validate unit name using regular expression to make sure it doesn't contain any of these characters"""
	if re.match("[@!#$%^&*()0-9*+=~`-/><;:[]]+"):
		return False
	return True


db.drop_all
db.create_all()
conversion1 = Celsius(c_id=1, unit_name='clss', unit_conversion_multiply = 1.8, unit_conversion_add = 32)
db.session.add_all([conversion1])
fahrenheit1 = Fahrenheit(f_id=2, unit_name='fhrnht', unit_conversion_divide = 0.56, unit_conversion_subtract = 32)
db.session.add_all([fahrenheit1])

db.session.commit()


@app.route('/wtf', methods = ['GET','POST'])
def wtf():
    form = TempForm()
    a = False
    if form.validate_on_submit():
        #return redirect(url_for(units))
        a = True
        val = 5
   # return render_template('TempWTF.html')
    return render_template('wtf.html', form=form, a = a) # d do not work
    #return render_template('layout.html') # i work


@app.route('/Homepage', methods = ['GET', 'POST'])
def HP():
    flash('hi')
    if request.method == 'POST':
        flash('post')
        if request.form['submit'] == 'CT':
            flash("hi there i can show")
            return redirect(url_for(('wtform')))
    return render_template('Homepage.html')

@app.route('/abc', methods = ['GET' , 'POST'])
def abc():
    #choices=[('cpp', 'c++'),('py','python')]
    form = MyForm()
    form.Conversion3.choices=[('cpp', 'c++'),('py','python')]
    a = False
    val = 0
    if form.validate_on_submit():
        return ("it Works")
    #return render_template('TempWTF.html')
    return render_template('wftTemp.html', form=form, a=a, val=val) # d do not work
    #return render_template('layout.html') # i work
@app.route('/')
def initial_page():
    return "hello World"

@app.route('/units')
def subsequent_page():
     return render_template('layout.html')


if __name__=='__main__':
    app.run()
