#Imaging for Raspberry Pi Camera by Tony Pham (May 7, 2021)

import RPi.GPIO as GPIO         #Import the GPIO library
import time 	                #Import the time library
from picamera import PiCamera   #Import the camera library

#Pin Info

GPIO.setmode(GPIO.BOARD)        #Set pin name mode
GPIO.setup(33, GPIO.OUT)
led = 33                        #Set pin 33 to pwm for excitation led

#Camera Settings (change these as desired)

camera = PiCamera(resolution=(1280,720), framerate=30)      #Set up the raspbery pi camera; can change resolution; framerate doesn't matter for image capture
camera.iso = 100                    #Set the ISO/sensitivity to desired value. 100 - 800
time.sleep(2)                       #Wait for the automatic gain control to settle
camera.shutter_speed = 10000		#Set the camera shutter speed in microseconds
camera.exposure_mode = 'off'		#Set auto exposure to off; change as desired
g = camera.awb_gains                #Save white balance settings after gain has adjusted
camera.awb_mode = 'off'             #Set auto white balance to off; change as desired
camera.awb_gains = g                #Restore auto white balance gains; remove if leaving auto white balance on

#Image Capture

GPIO.output(ledEx, GPIO.HIGH)		#Start led
time.sleep(2)
camera.capture('{timestamp}.jpg')	#Capture image; change naming scheme or format if desired
time.sleep(2)
GPIO.output(ledEx, GPIO.LOW)        #Stop led
GPIO.cleanup()                      #Reset pins

print("DONE")                       #Signal completion of program
