from flask import Flask
import inspect
from flask import render_template
import os

app = Flask(__name__)
# @app.route('/')
# def hello_world():
# 	return 'Hello World!'

@app.route('/')
def hello():
    return render_template('index.html')

# @app.route('/favicon.ico')
# def favicon():
#     return url_for('static', filename='favicon.ico')

if __name__ == '__main__':
 	app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
#   print inspect.getsource(Bootstrap)
