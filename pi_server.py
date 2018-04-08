from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

classToLed = [24, 25, 8, 7, 12]

def switchOnLed(type):
	GPIO.output(classToLed[type], True)

def switchOffLed(type):
	GPIO.output(classToLed[type], False)

def resetLed():
	for i in range(0, 5):
		GPIO.output(classToLed[i], False)
		time.sleep(0.2)

def testLights():
	for i in range(0, 5):
		print ("light up", i)
		switchOnLed(i)
		time.sleep(2)
		switchOffLed(i)

def setup():
	GPIO.setmode(GPIO.BCM)
	#Button to GPIO23
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)	
	#Led
	GPIO.setup(24, GPIO.OUT)
	GPIO.setup(25, GPIO.OUT)  
	GPIO.setup(8, GPIO.OUT)  
	GPIO.setup(7, GPIO.OUT)  
	GPIO.setup(12, GPIO.OUT)

@app.route('/glowled', methods = ['GET', 'POST'])
def glow_led():
	predictedClass = request.args.get('class')
	print ('Got class', predictedClass)

	resetLed()
	switchOnLed(predictedClass)

	return 'Pi task ended'
	

if __name__ == '__main__':
	setup()

	resetLed()
	switchOnLed(4)

	app.run(host="0.0.0.0", port=5000, debug=False)
