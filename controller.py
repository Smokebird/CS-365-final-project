from flask import Flask, render_template, request, redirect, url_for, abort, session
import unitsenv
app= Flask(__name__)
app.config['SECRET_KEY'] = 'LUTHERCOLLEGE'
@app.route('/')
def home():
	return "cs365 final project!"

@app.route('/default_units')
def default_units(units_page):
	return render_template('layout.html')

@app.route('/calculations', methods=['POST'])
def calculations():
	#session['something_here']= request.form['MyForm']
	#session['something_here']= request.form['something_else_here']
	#if statement to handle user's choice of conversions from the buttons clicked on page
	#if user selects fahrenheit to celsius, do some calculations here, else do some other calculations
	convert_val1 = Celsius.query.filter(Celsius.unit_conversion_multiply).first()
	convert_val2 = Celsius.query.filter(Celsius.unit_conversion_add).first() 
	convert_val3 = Fahrenheit.query.filter(Fahrenheit.unit_conversion_divide).first()
	convert_val4 = Fahrenheit.query.filter(Fahrenheit.unit_conversion_subtract).first() 
	convert_val5 = Kelvin.query.filter(Kelvin.unit_conversion_frac).first()
	convert_val6 = Kelvin.query.filter(Kelvin.unit_conversion_num).first() 
	convert_val7 = Kelvin.query.filter(Kelvin.unit_conversion_frac).second()
	convert_val8 = Kelvin.query.filter(Kelvin.unit_conversion_num).second() 
	#calculations done here
	#still needs to be completed for custom cases
	if intial_unit == 'celsius':
		if conversion_unit == 'fahrenheit':
			conversion_val = (number * convert_val1) + convert_val2
		else if conversion_unit == 'kelvin':
			conversion_val = (number * convert_val5) + convert_val6
		else
			conversion_val = (number) #some calculation specified by user

	else if initial_unit == 'fahrenheit':
		if conversion_unit == 'celsius':
			conversion_val = (number * convert_val3) - convert_val4
		else if conversion_unit = 'kelvin':
			conversion_val = (number * convert_val7) + convert_val8

	else if initial_unit == 'kelvin':
		if conversion_unit == 'celsius':
			convert_val = (number * convert_val5) - convert_val6
		else if conversion_unit == 'fahrenheit':
			convert_val = (number * convert_val7) - convert_val8
		else
		conversion_val = (number) #some custom unit calculations here

	else if initial_unit = 'other_custom_unit':
		convert_val = (number) #some calculation specified by user
#this last part probably not necessary, since it's done in the other file
@app.route('/custom_units', methods=['POST'])
def custom_units(units_page_two):
	session['custom_unit'] = request.form['something_here']
	session['convert_to'] = request.form['something_here_as_well']
	return redirect(url_for('units_response'))

@app.route('/convert_to')
def convert_to():
	if not 'custom_unit' in session:
		return abort(403)

	return render_template('something.html', custom_unit = session['something_here'], custom_unit = ['custom_unit'])

if __name__ == '__main__':
	app.run(debug=True)
