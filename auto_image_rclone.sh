#!/bin/bash

# set current date
DATE=$(date +%F@%H:%M:%S)

# load in the files from the cloud server
rclone sync -v onedriveTest:"CF Imaging RPi" /home/pi/rclone/

# run the imaging script
python /home/pi/MIPI_Camera/RPI/python/rclone-camera-test.py

# process the image (skipped for now)


# move the processed (unprocessed) image to the synced folder
echo $DATE
mv /home/pi/rclone-test.jpg /home/pi/rclone/$DATE.jpg

# upload the files back to the cloud server
rclone sync -v /home/pi/rclone/ onedriveTest:"CF Imaging RPi"

