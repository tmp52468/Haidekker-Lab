#Fluorescence Image Test for Raspberry Pi Camera

import RPi.GPIO as GPIO           #Import the GPIO library
import time                       #Import the time library
from picamera import PiCamera     #Import the camera library

GPIO.setmode(GPIO.BOARD)          #Set pin name mode
GPIO.setup(32, GPIO.OUT)          
pwmAct = GPIO.PWM(32, 1000)       #Set pin 32 to pwm for actinic led
GPIO.setup(33, GPIO.OUT)
pwmEx = GPIO.PWM(33, 1000)        #Set pin 33 to pwm for excitation led

camera = PiCamera()               #Set up the raspberry pi camera

#Main Program     

dc = 50                           #Set the duty cycle of pwm for pins
pwmAct.start(dc)                  #Start actinic led at duty cycle
time.sleep(10)                    #Wait 10 seconds for plant to react

camera.capture('Actinic.jpg')     #Capture actinic image

pwmEx.start(dc)                   #Start excitation led at duty cycle

camera.capture('Excitation.jpg')  #Capture excitation image

pwmEx.stop()                      #Stop excitation led
pwmAct.stop()                     #Stop actinic led
GPIO.cleanup()                    #Reset pins

print("DONE")
