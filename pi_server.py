from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
from tester import runTest

app = Flask(__name__)
	
@app.route('/glowled', methods = ['GET', 'POST'])
def glow_led():
	print ("hello in api")
	

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=False)
