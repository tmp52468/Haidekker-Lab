#!/bin/bash

# set current date
DATE=$(date +%F@%H:%M:%S)

# load in the files from the cloud server
rclone sync -v onedrive:PathToOneDriveFolder /home/pi/rclone/

# run the imaging script
python /home/pi/MIPI_Camera/RPI/python/cf_imaging.py

# process the image (skipped for now)


# move the processed (unprocessed) image to the synced folder
echo $DATE
mv /home/pi/cf_image.jpg /home/pi/rclone/$DATE.jpg

# upload the files back to the cloud server
rclone sync -v /home/pi/rclone/ onedriveTest:NameOfOneDriveFolder

