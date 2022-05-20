from flask import Flask,render_template

app= Flask(__name__)
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")	

@app.route('/employeelist')
def employeelist():
	return render_template("employeelist.html")	

@app.route('/newemployee')
def newemployee():
	return render_template("newemployee.html")	