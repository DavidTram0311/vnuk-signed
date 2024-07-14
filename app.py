from flask import Flask, render_template, request, redirect, url_for, send_file, flash
import os
from utils import subtitle
from utils import create_gif
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

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
            # Check video id in the folder gif
            files = os.listdir(gif_dir)
            if f"{url}.gif" in files:
                return redirect(url_for("translated", url=url))

            # create a pose GIF for the video subtitle string, if video id not in the folder gif
            success, subtitle_string= subtitle(url)
            if success:
                create_gif(subtitle_string=subtitle_string, gif_dir=f"static/images/gif", url=url)
                return redirect(url_for("translated", url=url))
            else:
                flash("We only support video that has subtitles", "error")
                return redirect(url_for('input_form'))

            # subtitle_string = subtitle(url)
            # create_gif(subtitle_string=subtitle_string, gif_dir=f"static/images/gif", url=url)
            # return redirect(url_for("translated", url=url))
    return render_template('input_form.html')


@app.route('/translated/<url>')
def translated(url):
    return render_template('translated.html', url=url)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
