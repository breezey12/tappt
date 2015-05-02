import sh
import sys
import os

url = sys.argv[1]
sh.cd("media_files")
sh.youtube_dl(url)
list_of_media_files = os.listdir(".")
file_to_rename = list_of_media_files[0]
os.rename(file_to_rename, "convert_me.mp4")
file_to_convert = "convert_me.mp4"
extract_audio_command = "ffmpeg -i " + file_to_convert + " -vn -ac 2 -ar 44100 -ab 320k -f mp3 " + file_to_convert[:-4] + ".mp3"
os.system(extract_audio_command)
