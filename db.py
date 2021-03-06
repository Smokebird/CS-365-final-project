from flask import Flask, render_template, redirect, request, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy.types as types
from flask_wtf import Form
from wtforms import TextField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired, Required


app = Flask(__name__)
app.debug = True
app.config['AQLALCHEMY_DATABASE_URI'] = 'sqlite:////temp/test.db'
db = SQLAlchemy(app)
app.secret_key = 'b\xdfp\xee-\xce\x9c\x15N]D\xb3\x01\x1f\x8a)!1x8x9\xc6R\x18y'
#class EqType(types.TypeDecorator):
 #   impl = types.Interger

#class Temp(db.Model):
 #   __tablename__ = 'course'


class CreateForm(Form):
    Conversion = TextField('Conversion', validators = [DataRequired()])
    unit1 = TextField('unit1', validators = [DataRequired()])
    unit2 = TextField('unit2', validators = [DataRequired()])

class MyForm(Form):
    number = TextField('number', validators = [DataRequired()])
   
    Conversion = SelectMultipleField('Conversion', validators=[Required()])
    Conversion2 = SelectMultipleField('Conversion2', choices=[('cpp', 'c++'),('py','Python')])
    Conversion3 = SelectMultipleField('Conversion3')

class TempForm(Form):
    myChoices=[('none',' '),('CF', 'Celsius to Fahrenheit'),('CK','Celsius to Kelvin'),('FC','Fahrenheit to Celsius'), ('FK', 'Fahrenheit to Kelvin'), ('KC', 'Kelvin to Celsius'),('KF','Kelvin to Fahrenheit')]
    Number = TextField('Number', validators=[DataRequired()])
   
    Con = SelectField('Conversion', choices=myChoices  ,validators=[Required()])    
    

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
#	'''validate unit name using regular expression to make sure it doesn't c#ontain any of these characters'''
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

@app.route('/create', methods =['GET','POST'])
def create():
    form=CreateForm()
    if form.validate_on_submit():
        return redirect('/units')
    return render_template('Creat.html', form=form)

#this is important
@app.route('/wtf', methods = ['GET','POST'])
def wtf():
    form = TempForm()
    a = False
    if form.validate_on_submit():
        return redirect("/units")
   # return render_template('TempWTF.html')
    return render_template('wtf.html', form=form, a = a) # d do not work
    #return render_template('layout.html') # i work


# this is important
@app.route('/Homepage', methods = ['GET', 'POST'])
def HP():

    #if request.form['submit'] == 'CT': # return bad request
    if request.method == "POST":
        if request.form['submit'] == 'CT':
            flash('posted')
            return redirect(url_for(('wtf')))
        else:
            return redirect('/create')
    return render_template('Homepage.html')


@app.route('/')
def initial_page():
    return "hello World"

@app.route('/units')
def subsequent_page():
     return render_template('layout.html')


if __name__=='__main__':
    app.run()
