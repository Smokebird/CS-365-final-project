from flask import Flask, render_template, redirect
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy.types as types
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['AQLALCHEMY_DATABASE_URI'] = 'sqlite:////temp/test.db'
db = SQLAlchemy(app)

#class EqType(types.TypeDecorator):
 #   impl = types.Interger

#class Temp(db.Model):
 #   __tablename__ = 'course'
    
class MyForm(Form):
    name = TextField('name', validators = [DataRequired()])

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
   # celsius = db.relationship('Celsius', secondary = conversion)


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

db.drop_all
db.create_all()
fahrenheit1 = Fahrenheit(f_id=2, unit_name='fhrnht', unit_conversion_divide = 0.56, unit_conversion_subtract = 32)
db.session.add_all([fahrenheit1])

db.session.commit()




@app.route('/wtf', methods = ('GET' , 'POST'))
def wtf():
    #form = MyForm()
    #if form.validate_on_submit():
     #   return ("it Works")
    return render_template('TempWTF.html')
    return render_template('wtfTemp.html') # d do not work
    return render_template('layout.html') # i work
@app.route('/')
def initial_page():
    return "hello World"

#@app.route('/units')
#def subsequent_page():
 #    return render_template('layout.html')


if __name__=='__main__':
    app.run()
