# views.py


from flask import Flask, flash, redirect, render_template, request,\
    session, url_for
from functools import wraps

app = Flask(__name__)
app.config.from_object('config')



@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        youtube_url = request.form['youtube_url']
        # TODO: get the speechmatics stuff to spit us back a list of urls
        stream_urls = ['dummy1', 'dummy2', 'dummy3']
        return render_template('stream.html', stream_urls=stream_urls)
