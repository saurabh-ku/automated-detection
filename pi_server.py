from flask import Flask, render_template, request
from werkzeug import secure_filename
import os

app = Flask(__name__)
	
@app.route('/glowled', methods = ['GET'])
def glow_led():
	print('hello 1')
	data = request.args.get('class')
	print ("hello in api", data)

	return None
	

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=False)
