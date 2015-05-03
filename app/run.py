from views import app
import os

if 'example.json' in os.listdir('speech/'):
    os.remove('speech/example.json')
for file in os.listdir('media_files/'):
    if ".mp4" in file or '.mp3' in file:
        full_path = 'media_files/'
        os.remove(os.path.join(full_path, file))
app.run(debug=True)
