from flask import Flask, render_template, request, redirect, url_for
import os
import shutil
from utils import *

app = Flask(__name__)

start = time.time()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/input_form', methods=['POST', 'GET'])
def input_form():
    if request.method == 'POST':
        url = request.form['youtube-url']
        url = url.replace('https://www.youtube.com/watch?v=', '') # get only the ID of the video
        print("YouTube video ID = {}".format(url))

        if url:
            gif_dir = "static/images/gif"
            # Ensure gif_dir exists
            if not os.path.exists(gif_dir):
                os.makedirs(gif_dir)
            # delete all files in the gif_dir gif (results of previous runtime)
            for filename in os.listdir(gif_dir):
                file_path = os.path.join(gif_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))

            # create a pose GIF for the video subtitle string
            subtitle_string = subtitle(url)
            create_gif(subtitle_string=subtitle_string, gif_dir=gif_dir)
            return redirect(url_for("translated", url=url))
    return render_template('input_form.html')


@app.route('/translated/<url>')
def translated(url):
    return render_template('translated.html', url=url)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
