#!/bin/bash

# variables
RCLONE="/home/pi/rclone" # Local Rclone directory for cloud sync
ONEDRIVE="<onedrive_name>:<path/to/onedrive/directory>" # OneDrive directory on cloud drive
SAMBA="/home/pi/smbshare/<subdirectory>" # SambaShare/CIFS directory
TYPE="single" # Type of analysis ('single' or 'multiple')

# set specific system name and current date
NAME=<nameofsystem>
DATE=$(date +%F@%H:%M)

# load in the files from the cloud server
rclone sync -v $ONEDRIVE $RCLONE/

# run the imaging script
python /home/pi/MIPI_Camera/RPI/python/cf_capture.py

# process the image
imagej -b /home/pi/CF_Imaging.ijm "/home/pi/cf_image.jpg $SAMBA/$NAME_$DATE $TYPE"
imagej -b /home/pi/CF_Imaging.ijm "/home/pi/cf_image.jpg $RCLONE/$NAME_$DATE $TYPE"

# move the processed (and unprocessed) image(s) to the synced fol$
cp /home/pi/cf_image.jpg $SAMBA/$NAME_$DATE.jpg
mv /home/pi/cf_image.jpg $RCLONE/$NAME_$DATE.jpg

# upload the files back to the cloud server
rclone sync -v $RCLONE/ $ONEDRIVE
