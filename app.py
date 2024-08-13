# I keep PHP in my FLASK - VintellX
# Why the hell am I using Flask? I don't know. I'm not even a Web Developer by profession. xD

from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint
from xdspotify import Vinify
from blogo import *
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/about')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    blogs = load_blogs()
    tags = tags_count()
    return render_template('blog.html', blogs=blogs, tags=tags)

@app.route('/blog/<blog_id>')
def blogo(blog_id):
    blogs=load_blogs()
    for blog in blogs:
        if blog['id'] == blog_id:
           title = blog['title']
           date = blog['info']['date']
           readtime = blog['info']['readtime']
           tags = [tag for tag in blog['info']['tags']]
    templato = f'blogo/{blog_id}.html'
    return render_template('blogbase.html', blogo=templato, title=title, date=date, readtime=readtime, tags=tags)

@app.route('/blog/tags/<tag>')
def blogTag(tag):
    blogs = load_blogs()
    tags = tags_count()
    tagged_blogs = [blog for blog in blogs if tag in blog['info']['tags']]
    totalblogs = len(tagged_blogs)
    return render_template('blogtag.html', blogs=tagged_blogs, tags=tags, tagItem=tag, totalblogs=totalblogs)


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
