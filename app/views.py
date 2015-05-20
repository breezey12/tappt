# views.py

#importing modules

from flask import Flask, flash, redirect, render_template, request,\
    session, url_for
from functools import wraps
from speech.locate_word import run_word_loc, get_words, locate_keywords, make_generic_youtube_url
import os

app = Flask(__name__)
app.config.from_object('config')

'''
The function homepage() tells the HTML form template to post a youtube_url 
and a single keyword temporarily to the server. If the youtube_url exists, 
the function then time stamps the youtube_url at the time in the video when
the specified keyword is spoken (if spoken at all). The function renders a new 
html file (youtube_embed.html) if the youtube_url and keyword exist.
'''

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        empty_results = False
        youtube_url = make_generic_youtube_url(request.form['youtube_url'])
        keyword = request.form['keyword']
        times = run_word_loc(youtube_url, app.config['SPEECHMATICS_API_KEY'], [keyword]) 
        youtube_urls = [[time_loc, youtube_url.replace('watch?v=', 'embed/') + "?start=" + str(time_loc)] for time_loc in times]
        if not youtube_urls:
            empty_results = True 
        return render_template('youtube_embed.html', 
            youtube_urls=youtube_urls,
            keyword=keyword,
            empty_results=empty_results)
