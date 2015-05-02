import sys
import os
import re
import time

def convert_yt_to_mp3(url):
    url = scrub_the_url(url)
    unique_file_id = url[-11:]
    full_path = "speech/media_files/" + unique_file_id + ".mp4"
    youtube_dl_command = "youtube-dl -o " + full_path + " " + url
    os.system(youtube_dl_command)
    convert_mp4_to_mp3(full_path)
    return full_path[:-1] + "3"

def convert_mp4_to_mp3(file_name):
    extract_audio_command = "ffmpeg -i " + file_name + " -vn -ac 2 -ar 44100 -ab 320k -f mp3 " +file_name[:-4] + ".mp3"
    os.system(extract_audio_command)
    

def scrub_the_url(url):
    if "s" == url[4]:
        url = url[:43]
    else:
        url = url[:42]
    return url
