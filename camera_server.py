from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
from tester import runTest
import requests

app = Flask(__name__)

ROOT_DIR = os.path.dirname(
			os.path.realpath(__file__)
			)
UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = os.path.join(
								ROOT_DIR,
								UPLOAD_FOLDER
								)

@app.route('/upload')
def upload_file():
	glowLedOnPi(2)
	return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file_completed():
	if request.method == 'POST':
		f = request.files['file']
		f.save(
			os.path.join(
				app.config['UPLOAD_FOLDER'], 
				secure_filename("img.jpg")
				)
			)

		predictedClass = runTest()
		glowLedOnPi(predictedClass)
		return 'ran inference, predicted class', predictedClass

def glowLedOnPi(predictedClass):
	addr = 'http://192.168.43.70:5000'
	test_url = addr + '/glowled'

	requests.post(test_url, data = {'class' : predictedClass})

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=False)
