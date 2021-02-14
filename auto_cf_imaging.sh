#!/bin/bash

# variables
RCLONE="/home/pi/rclone" # Local Rclone directory for cloud sync
ONEDRIVE="<onedrive_name>:<path/to/onedrive/directory>" # OneDrive directory on cloud drive
SAMBA="/home/pi/smbshare/<subdirectory>" # SambaShare/CIFS directory
TYPE="single" # Type of analysis ('single' or 'multiple')

# set specific system name and current date
NAME=<nameofsystem>
DATE=$(date +%F@%H)

# load in the files from the cloud server
rclone sync -v $ONEDRIVE $RCLONE/

sleep 1s

# run the imaging script
python /home/pi/MIPI_Camera/RPI/python/cf_capture.py

sleep 1s

mv /home/pi/cf_image.jpg /home/pi/CF_Images/cf_image.jpg

# process the image
imagej -x 1000 -i /home/pi/CF_Images/cf_image.jpg -b /home/pi/CF_Imaging.ijm "/home/pi/CF_Images/$NAME_$DATE $TYPE"

sleep 5s

# move the processed (and unprocessed) image(s) to the synced fol$
mv /home/pi/CF_Images/cf_image.jpg /home/pi/CF_Images/$NAME_$DATE.jpg
cp /home/pi/CF_Images/* $SAMBA/
mv /home/pi/CF_Images/* $RCLONE/

sleep 1s

# upload the files back to the cloud server
rclone sync -v $RCLONE/ $ONEDRIVE
