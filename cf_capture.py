import arducam_mipicamera as arducam
import v4l2 #sudo pip install v4l2
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(32, GPIO.OUT)
#pwmAct = GPIO.PWM(32, 1000)
GPIO.setup(33, GPIO.OUT)
pwmEx = 33

def set_controls(camera):
    #try:
        # print("Reset the focus...")
        # camera.reset_control(v4l2.V4L2_CID_FOCUS_ABSOLUTE)
    #except Exception as e:
        # print(e)
        # print("The camera may not support this control.")

    try:
	print("Setting the Exposure...")
	camera.set_control(v4l2.V4L2_CID_EXPOSURE, 2500)
	print("Setting the Gain...")
	camera.set_control(v4l2.V4L2_CID_GAIN, 3) #Range 0-15
        print("Disable Auto Exposure...")
        camera.software_auto_exposure(enable = False)
        #print("Disable Auto White Balance...")
        #camera.software_auto_white_balance(enable = False)
	#print("Adjusting Gain...")
	#camera.manual_set_awb_compensation(rGain = 0, bGain = 0)
	#print("Reading strobe register...")
        #strobeValue = camera.read_sensor_reg(address = 0x3006)
	#print(strobeValue)
        #print("Setting strobe output...")
        #camera.write_sensor_reg(address = 0x3006, value = 1)
        #strobeValue = camera.read_sensor_reg(address = 0x3006)
        #print(strobeValue)
        #camera.write_sensor_reg(address = 0x3928, value = 0xFF)
        #print("Reading strobe setting register...")
        #strobeSetting = camera.read_sensor_reg(address = 0x3928)
        #print(strobeSetting)

    except Exception as e:
        print(e)

dc = 50

if __name__ == "__main__":
    try:
        camera = arducam.mipi_camera()
        print("Open camera...")
        camera.init_camera()
        #print("Setting the resolution...")
        #fmt = camera.set_resolution(1920, 1080)
        #print("Current resolution is {}".format(fmt))
        # print("Start preview...")
        # camera.start_preview(fullscreen = False, window = (0, 0, 1280, 720))
        set_controls(camera)
	time.sleep(1)

	#pwmAct.start(dc)
	#time.sleep(10)

        #frame = camera.capture(encoding = 'jpeg')
        #frame.as_array.tofile("actinic.jpg")
	#set_controls(camera)

	GPIO.output(pwmEx, GPIO.HIGH)

        time.sleep(1)

        #print("Current resolution is {}".format(fmt))
        frame = camera.capture(encoding = 'jpeg')
        frame.as_array.tofile("cf_image.jpg")

	time.sleep(1)

	GPIO.output(pwmEx, GPIO.LOW)
	#pwmAct.stop()

        # Release memory
        del frame
        # print("Stop preview...")
        # camera.stop_preview()
        print("Close camera...")
        camera.close_camera()
	GPIO.cleanup()
	print("DONE")

    except Exception as e:
        print(e)
