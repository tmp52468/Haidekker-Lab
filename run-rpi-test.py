#Fluorescence Imaging for Raspberry Pi Camera

import RPi.GPIO as GPIO		#Import the GPIO library
import time 			#Import the time library
from picamera import PiCamera	#Import the camera library

GPIO.setmode(GPIO.BOARD)	#Set pin name mode
#GPIO.setup(32, GPIO.OUT)
#pwmAct = GPIO.PWM(32, 1000)	#Set pin 32 to pwm for actinic led
GPIO.setup(33, GPIO.OUT)
ledEx = 33			#Set pin 33 to pwm for excitation led

camera = PiCamera(resolution=(1280,720), framerate=30)	#Set up the raspbery pi camera


#Main Program
camera.iso = 100			#Set the ISO/sensitivity to desired value. 100 - 800
time.sleep(2)				#Wait for the automatic gain control to settle
#print(camera.exposure_speed)
camera.shutter_speed = 10000		#Set the camera shutter speed in microseconds
camera.exposure_mode = 'off'		#Set auto exposure to off
g = camera.awb_gains
camera.awb_mode = 'off'			#Set auto white balance to off
camera.awb_gains = g			#Restore auto white balance gains

#dc = 50					#Set the desired duty cycle of pwm pins
#pwmAct.start(dc)			#Start actinic led at duty cycle
#time.sleep(600)			#Wait 10 minutes for plant to react

camera.capture('Actinic.jpg')		#Capture actinic image

GPIO.output(ledEx, GPIO.HIGH)		#Start excitation led at duty cycle

camera.capture('Excitation.jpg')	#Capture excitation image

GPIO.output(ledEx, GPIO.LOW)				#Stop excitation led
#pwmAct.stop()				#Stop actinic led
GPIO.cleanup()				#Reset pins

print("DONE")				#Signal completion of program

