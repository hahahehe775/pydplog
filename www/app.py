from flask import Flask, render_template, request
from transwarp import getlocation
from log import Log
import os

app = Flask(__name__)
# @app.route('/')
# def hello_world():
# 	return 'Hello World!'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        service_name = request.form['service']
        warname_name = request.form['warname']
        today = request.form['today']
        anhourago = request.form['anhourago']
        rightnow = request.form['rightnow']
        locationList = getlocation.getlocation('./transwarp/pydplog.db', service_name, warname_name)
        instanceTitles = []
        for j in locationList:
            instanceTitle = j[1] + "@" + j[0]
            instanceTitles.append(instanceTitle)
        return render_template('index.html', instanceTitles = instanceTitles)
    else:    
        return render_template('index.html')

# @app.route('/favicon.ico')
# def favicon():
#     return url_for('static', filename='favicon.ico')

if __name__ == '__main__':
  	app.run(host='0.0.0.0', port=8080, debug=True)