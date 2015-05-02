
import json

file_path = 'example.json'
keywords = ["accountability", "accountable"]

def get_words(file_path):
    """returns list of words with attributes (time, confidence)"""
    with open(file_path) as raw_json:    
        word_dict = json.load(raw_json)
    word_list = word_dict['words']

    #format of word_list: [u'duration': u'0.280', u'confidence': u'0.995', u'name': u'things', u'time': u'2.797']
    return word_list

def locate_keywords(word_list, keywords):
    """returns times keyword(s) occur"""
    i = 0 
    times = []
    for word in word_list:
        i += 1
        if i > 5000: break
        if word['name'].lower() in keywords:
            times.append(word['time'])
    return times

def round_seconds(sec):
    """rounds and returns 10 secs earlier"""
    sec = int(float(sec))
    if sec - 10 < 0:
        sec = 0
    else: sec = sec -10
    return sec


