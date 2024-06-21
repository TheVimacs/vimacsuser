# I keep PHP in my FLASK - VintellX
# Why the hell am I using Flask? I don't know. I'm not even a Web Developer by profession. xD

from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint
from xdspotify import Vinify
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/about')
def index():
    return render_template('index.html')

@app.route('/pubkey')
def pubkey():
    return render_template('pubkey.html')

@app.route('/projects')
def projects():
    json_data = open('static/assets/projects.json')
    data = json.load(json_data)
    json_data.close()
    total = 0
    github = 0
    web = 0
    youtube = 0

    for project in data:
        if 'links' in project:
            if project['links'].get('web'):
                web += 1
                total += 1
            if project['links'].get('github'):
                github += 1
                total += 1
            if project['links'].get('youtube'):
                youtube += 1
                total+= 1
    return render_template('projects.html', projects=data, total=total, github=github, web=web, youtube=youtube)

@app.route('/spotify')
def spotify():
    vinify = Vinify()
    texto, xdimage = vinify.fetchhtml()
    return render_template('spotify.html', xdimage=xdimage, texto=texto)

if __name__ == '__main__':
    app.run(debug=True)
