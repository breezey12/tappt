
#return time (s) where word occurs

import json

with open('example.json') as raw_json:    
    word_dict = json.load(raw_json)

word_list = word_dict['words']

keywords = ["accountability", "accountable"]

#format of word_list: [u'duration': u'0.280', u'confidence': u'0.995', u'name': u'things', u'time': u'2.797']
i = 0 
for word in word_list:
    i += 1
    if i > 5000: break
    if word['name'].lower() in keywords:
        print word['time']

#round down seconds


#youtube url starting at word (or 10 sec before)
