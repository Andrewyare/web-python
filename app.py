from flask import Flask, render_template
from user_agent import generate_user_agent
from datetime import datetime
import os

app = Flask(__name__)

user = generate_user_agent()
now = datetime.now()

time = now.strftime("%H:%M")

os = os.name

menu = ["Flask", "Is", "Great"]
text = 'Some quick example text to build on the card title and make up the bulk of the card`s content.'

@app.route('/')
def index():
	return render_template("index.html", title = "Flask",text = text, time = time,os=os) 

@app.route('/home')
def home():
	return render_template("index.html", title = "Flask",text = text, time = time,os=os) 

@app.route('/about')   
def about():
	return render_template('about.html',menu = menu,user = user,time = time,os=os)

@app.route('/contact')
def contact():
	return render_template('about.html',menu = menu,user = user,time = time,os=os)

if(__name__=='__main__'):
	app.run(debug=True)

