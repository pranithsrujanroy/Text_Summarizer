#from flask import Flask, render_template, request
#from query import QueryService
#from flask_restful import Api, Resource, reqparse
from flask import Flask, render_template, send_from_directory, request
import script
import text_script
import  speechc_script
import os
app = Flask(__name__,template_folder='templates')
#api=Api(app)

@app.route("/")
def home():
    return render_template("index.html")
	
@app.route('/audio', methods=['POST'])
def audio():
    audio_name=request.form['audio']
    # working_dir = os.path.dirname(os.path.realpath(__file__))
    # pyglet.resource.path = [os.path.join(working_dir,audio)]
    # pyglet.resource.reindex()
    # music = pyglet.resource.media(str(os.path.realpath('.')+'\\'+audio))
    # music.play()
    # pyglet.app.run()
    speechc_script.get_audio(audio_name)
    return render_template('url.php')

@app.route('/text', methods=['POST'])
def text():
    file_name=request.form['text']
    text_script.get_text(file_name)
    return render_template('url.php')

@app.route('/url', methods=['POST'])
def url():
    url_var=request.form['url_var']
    script.get_url(url_var)
    return render_template('url.php')
if __name__ == "__main__":
    try:
        app.run('localhost', port = 5000, debug = True, use_reloader = False)
    except getopt.GetoptError as e:
        print (e)