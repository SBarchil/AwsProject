from flask import Flask,render_template

app= Flask(__name__)
@app.route('/')
def index():
	title="Aws Projects 001"
	return render_template("index.html", title=title)

@app.route('/contact')
def contact():
	names= ["Said", "Susan", "Aicha", "Khalid"]
	return render_template("contact.html", names=names)	

@app.route('/employeelist')
def employeelist():
	return render_template("employeelist.html")	

@app.route('/newemployee')
def newemployee():
	return render_template("newemployee.html")	