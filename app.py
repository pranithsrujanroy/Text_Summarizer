#from flask import Flask, render_template, request
#from query import QueryService
#from flask_restful import Api, Resource, reqparse
from flask import Flask, render_template, send_from_directory, request
app = Flask(__name__,template_folder='templates')
#api=Api(app)

@app.route("/")
def home():
    return render_template("index.html")
	
@app.route('/audio', methods=['GET', 'POST'])
def audio():
    return render_template('audio.php')

@app.route('/text', methods=['GET', 'POST'])
def text():
    return render_template('text.php', say=request.form['say'], to=request.form['to'])

@app.route('/url', methods=['GET', 'POST'])
def url():
    return render_template('url.php')

if __name__ == "__main__":
    try:
        app.run('localhost', port = 5000, debug = True, use_reloader = False)
    except getopt.GetoptError as e:
        print (e)