
import json, os
from download_yt import convert_yt_to_mp3
from speechmatics import SpeechmaticsClient
import time

def get_words(file_path):
    """returns list of words with attributes (time, confidence)"""
    with open(file_path) as raw_json:    
        word_dict = json.load(raw_json)
    word_list = word_dict['words']

    #format of word_list: [u'duration': u'0.280', u'confidence': u'0.995', u'name': u'things', u'time': u'2.797']
    return word_list

def round_seconds(sec):
    """rounds and returns 5 secs earlier"""
    sec = int(float(sec))
    if sec - 1 < 0:
        sec = 0
    else: sec = sec - 1
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

def call_speechmatic_api(audio_file_path, api_token, unique_json_id):
    """creates json word_list and returns its path""" 
    #syntax: speechmatics.py -f example.mp3 -l en-US -i 1049 -t Y2E4OGM3NzItOGMwZi00OGQyLTk3MDctY2FmYWE3ZmYxZmNk -o example.json
    c = "python speech/speechmatics.py -f " + audio_file_path + " -l en-US -i 1049 -t " + api_token + " -o " + unique_json_id 
    os.system(c)
    return 


def send_audio_to_speechmatics(audio_file_path, api_token, api_user_id, unique_json_id):
    """this should replace call_speechmatic_api"""
    client = SpeechmaticsClient(api_user_id, api_token)
    print "Uploading audio file: "+audio_file_path
    (directory, filename) = os.path.split(os.path.abspath(audio_file_path))
    language = "en-US"
    job_id = client.upload_audio(directory, filename, language)
    if job_id != None:
        print "New job started with id: "+str(job_id)
    else:
        print "Connection Failure"
        exit(1)

    details = client.get_job_details(job_id)

    if details == None:
        print "Connection Failure"
        exit(1)

    oldStatus="NotStarted"
    while details['job_status'] != 'done' and details['job_status'] != 'expired' and details['job_status'] != 'unsupported_file_format':
        if oldStatus != details['job_status']:
          print "Transcription in progress, "+details['job_status']
        oldStatus = details['job_status']
        epoch_now = int(time.time()) 
        wait_s = details['next_check'] - epoch_now
        #print "waiting requested check back time of "+str(wait_s)+"s"
        time.sleep(wait_s)
        details = client.get_job_details(job_id)
        if details == None:
            print "Connection Failure"
            exit(1)

    if details['job_status'] == 'unsupported_file_format':
      print "File was in an unsupported file format and could not be transcribed."
      print "You have been reimbursed all credits for this job."
  
    else:
      print "Transcription complete, downloading transcription"
      transcript = client.get_transcription(job_id, False)
      f = open(unique_json_id, 'wt')



def extract_unique_id_from_url(url):
    """extracts 11-digit video ID from the four different prefixes it may have
    from different YouTube URL formats"""
    characters_that_appear_just_before_unique_id = ["v=",
                                                    "/v/",
                                                    "/embed/",
                                                    "youtu.be/"]
    for characters in characters_that_appear_just_before_unique_id:
        if characters in url:
            start_of_unique_id = url.find(characters) + len(characters)
            return url[start_of_unique_id:start_of_unique_id + 11].encode("utf-8")
        else:
            print "did not find unique_id"


def make_generic_youtube_url(url):
    """takes one of the four different formats of YouTube URL and returns
    the canonical format"""
    id = extract_unique_id_from_url(url)
    return "http://youtube.com/watch?v=" + id


def run_word_loc(url, api_token, api_user_id, keywords):
    """
    checks to see if there's already a JSON file for this YouTube video ID.
    if there isn't, it downloads the media, sends it to Speechmatic, then 
    calls locate_keywords() to return a list of where the keyword was found
    """
    unique_id = extract_unique_id_from_url(url)
    unique_json_id = "speech/" + unique_id + ".json"
    url = "http://youtube.com/watch?v=" + unique_id
    if unique_id + ".json" not in os.listdir('speech/'):
        audio_file_path = convert_yt_to_mp3(url)
        call_speechmatic_api(audio_file_path, api_token, api_user_id, unique_json_id)
        clear_out_media_files()
    return locate_keywords(get_words(unique_json_id), keywords)


def clear_out_media_files():
     for file_name in os.listdir('speech/mediafiles/'):
         if file_name[-4:] == ".mp4" or file_name[-4:] == '.mp3':
             full_path = 'speech/mediafiles/'
             os.remove(os.path.join(full_path, file_name))
