import sh
import sys
import os
import re

def convert_youtube_to_mp3(url):
    url = scrub_the_url(url)
    # define the path where the media files are
    full_path = "speech/media_files"
    os.chdir(full_path)
    # downloads the YouTube via using shell application "Youtube-dl"
    sh.youtube_dl(url)
    # define the filename that should be renamed as the most recent file added to this directory
    unique_file_identifier = url[-11:]
    # make a list of files in the path
    list_of_files = os.listdir(full_path)
    # select the file just downloaded for conversion to mp3
    for some_file in list_of_files:
        if unique_file_identifier in some_file:
            the_downloaded_file = some_file
    convert_mp4_to_mp3(the_downloaded_file)
    return os.path.join(full_path,the_downloaded_file)


def convert_mp4_to_mp3(file):
    extract_audio_command = "ffmpeg -i " + file + " -vn -ac 2 -ar 44100 -ab 320k -f mp3 " +file[:-4] + ".mp3"
    os.system(extract_audio_command)
    

def scrub_the_url(url):
    if "s" == url[4]:
        url = url[:42]
    else:
        url = url[:41]
    return url
