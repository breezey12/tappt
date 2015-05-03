from views import app
import os

if 'example.json' in os.listdir('speech/'):
    os.remove('speech/example.json')
for file in os.listdir('speech/media_files/'):
    if file[-4:] == ".mp4" or file[-4:] == '.mp3':
        full_path = 'speech/media_files/'
        os.remove(os.path.join(full_path, file))
app.run(debug=True)
