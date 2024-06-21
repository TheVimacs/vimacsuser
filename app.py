# I keep PHP in my FLASK - VintellX
# Why the hell am I using Flask? I don't know. I'm not even a Web Developer by profession. xD

from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint
from xdspotify import Vinify


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def index2():
    return render_template('index.html')

@app.route('/spotify')
def spotify():
    vinify = Vinify()
    texto, xdimage = vinify.fetchhtml()
    return render_template('spotify.html', xdimage=xdimage, texto=texto)

if __name__ == '__main__':
    app.run(debug=True)
