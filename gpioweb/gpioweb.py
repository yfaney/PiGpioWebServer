#!/usr/bin/python
# Copyright (c) 2015 Younghwan Jang
# Author : Younghwan Jang

from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO
import json
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
#GPIO.setup(11, GPIO.OUT)
#GPIO.setup(12, GPIO.OUT)
#GPIO.setup(13, GPIO.OUT)
#GPIO.setup(15, GPIO.OUT)
#GPIO.setup(16, GPIO.OUT)
#GPIO.setup(18, GPIO.OUT)
#GPIO.setup(22, GPIO.OUT)
GPIO.output(4, False)
#GPIO.output(11, False)
#GPIO.output(12, False)
#GPIO.output(13, False)
#GPIO.output(15, False)
#GPIO.output(16, False)
#GPIO.output(18, False)
#GPIO.output(22, False)

pin = { '4' : False , '7' : False }

now = datetime.datetime.now()
timeString = now.strftime("%Y-%m-%d %H:%M")

@app.route("/")
def hello():
   templateData = {
      'title' : 'Remote Switch',
      'time': timeString
      }
   return render_template('gpioweb.html', **templateData)

@app.route("/hello")
def helloworld():
	return "hello world!"

@app.route("/4/on")
def action4on():
    GPIO.output(4, True)
    message = "GPIO 4 was turned on."
    templateData = {
        'message' : message,
        'time' : timeString
    }
    return render_template('gpioweb.html', **templateData)

@app.route("/api/4/on")
def api4on():
	GPIO.output(4, True)
	message = "GPIO 4 turned on."
	pin['4'] = True
	data = {"message": message, "result": True}
	return json.dumps(data)

@app.route("/api/4/off")
def api4off():
	GPIO.output(4, False)
	message = "GPIO 4 turned off."
	pin['4'] = False
	data = {"message": message, "result": True}
	return json.dumps(data)

@app.route("/api/get/4")
def get4():
	data = {"pinno" : 4, "output": pin['4']}
	return json.dumps(data)
	    
@app.route("/4/off")
def action4off():
    GPIO.output(4, False)
    message = "GPIO 4 was turned off."
    templateData = {
        'message' : message,
        'time' : timeString
    }
    return render_template('gpioweb.html', **templateData)
#@app.route("/all/on")
def actionallon():
    GPIO.output(7, True)
    GPIO.output(11, True)
    GPIO.output(12, True)
    GPIO.output(13, True)
    GPIO.output(15, True)
    GPIO.output(16, True)
    GPIO.output(18, True)
    GPIO.output(22, True)
    message = "All GPIO pins were turned on."
    templateData = {
        'message' : message,
        'time' : timeString
    }
    return render_template('gpioweb.html', **templateData)

#@app.route("/all/off")
def actionalloff():
	GPIO.output(7, False)
	GPIO.output(11, False)
	GPIO.output(12, False)
	GPIO.output(13, False)
	GPIO.output(15, False)
	GPIO.output(16, False)
	GPIO.output(18, False)
	GPIO.output(22, False)
	message = "All GPIO pins were turned off."
	templateData = {
		'message' : message,
		'time' : timeString
	}
	return render_template('gpioweb.html', **templateData)

if __name__ == "__main__":
	try:
		app.run(host="0.0.0.0", port=80, debug=True, threaded=True)
	except KeyboardInterrupt:
		GPIO.cleanup()
		print "GPIO pins cleaned up due to KeyboardInterrupt"
	finally:
		GPIO.cleanup()
		print "GPIO pins cleaned up"
