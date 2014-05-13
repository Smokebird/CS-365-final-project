
from flask import Flask, render_template, redirect, request, session, url_for
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy.types as types
from flask_wtf import Form
from wtforms import TextField, SelectField
from wtforms.validators import DataRequired

class TempForm(Form):
    Number = TextField('Number', validators=[DataRequired()])
    Con = SelectField('Conversion', validators=[DataRequired()])

app = Flask(__name__)
app.debug = True
app.config['AQLALCHEMY_DATABASE_URI'] = 'sqlite:////temp/test.db'
db = SQLAlchemy(app)
app.secret_key='hilsdkfjlfsdlj;kfdljkdfskjl'


#class EqType(types.TypeDecorator):
 #   impl = types.Interger

#class Temp(db.Model):
 #   __tablename__ = 'course'
    

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



@app.route('/units')
def subsequent_page():
     return render_template('layout.html')


if __name__ =='__main__':
    app.run()
