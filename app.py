from flask import Flask, render_template, request, redirect, url_for
import time
from pose_format import Pose
from pose_format.pose_visualizer import PoseVisualizer
import os
import shutil
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

start = time.time()

def subtitle(video_id):
    '''
    This function retrieve full subtitle in the youtube video
    input: video_id
    output: string (subtitle)
    '''
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    output = ''
    for x in transcript:
        sentence = x['text']
        output += f' {sentence}'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input_form', methods=['POST', 'GET'])
def input_form():
    if request.method == 'POST':
        url = request.form['youtube-url']
        url = url.replace('https://www.youtube.com/watch?v=', '')
        print(url)
        if url:
            folder = "static/images/gif"
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
            with open(f"assets/pose/{}.pose", "rb") as f:
                pose = Pose.read(f.read())
            v = PoseVisualizer(pose)
            v.save_gif("static/images/gif/pose.gif", v.draw())
            return redirect(url_for("translated", url=url))
    return render_template('input_form.html')


@app.route('/translated/<url>')
def translated(url):
    return render_template('translated.html', url=url)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
