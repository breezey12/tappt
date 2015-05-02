
import json, os
import download_yt

audio_file_path = 'media_files/video_30_seconds_1.mp3'
keywords = ["accountability", "accountable"]
api_token = "Y2E4OGM3NzItOGMwZi00OGQyLTk3MDctY2FmYWE3ZmYxZmNk"

def get_words(file_path):
    """returns list of words with attributes (time, confidence)"""
    with open(file_path) as raw_json:    
        word_dict = json.load(raw_json)
    word_list = word_dict['words']

    #format of word_list: [u'duration': u'0.280', u'confidence': u'0.995', u'name': u'things', u'time': u'2.797']
    return word_list

def round_seconds(sec):
    """rounds and returns 10 secs earlier"""
    sec = int(float(sec))
    if sec - 10 < 0:
        sec = 0
    else: sec = sec -10
    return sec

def locate_keywords(word_list, keywords):
    """returns times keyword(s) occur"""
    i = 0 
    times = []
    for word in word_list:
        i += 1
        if i > 5000: break
        if word['name'].lower() in keywords:
            times.append(round_seconds(word['time']))
    return times

def call_speechmatic_api(audio_file_path, api_token):
    """creates json word_list and returns its path""" 
    #syntax: speechmatics.py -f example.mp3 -l en-US -i 1049 -t Y2E4OGM3NzItOGMwZi00OGQyLTk3MDctY2FmYWE3ZmYxZmNk -o example.json
    c = "python speechmatics.py -f " + audio_file_path + " -l en-US -i 1049 -t " + api_token + " -o example.json"
    os.system(c)
    return "example.json"

def run_word_loc(audio_file_path, api_token, keywords):
    file_path = call_speechmatic_api(audio_file_path, api_token)
    return locate_keywords(get_words(file_path), keywords)
    



