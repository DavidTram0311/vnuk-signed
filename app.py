from flask import Flask, render_template, request, jsonify, redirect, url_for
import time




app = Flask(__name__)

start = time.time()


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
            return redirect(url_for("translated", url=url))
    return render_template('input_form.html')


@app.route('/translated/<url>')
def translated(url):
    return render_template('translated.html', url=url)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
