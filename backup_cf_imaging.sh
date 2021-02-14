#!/bin/bash

# variables
RCLONE="/home/pi/rclone" # Rclone directory for cloud sync
ONEDRIVE="onedrive:Pipeline_Test" # OneDrive directory on cloud drive
SAMBA="/home/pi/smbshare/Pipeline_Test" # SambaShare/CIFS directory
TYPE="single" # Type of analysis (single or multiple)

# set current date
NAME="Pipeline_Test"
DATE=$(date +%F@%H)

# load in the files from the cloud server
rclone sync -v $ONEDRIVE $RCLONE/

sleep 1s

# process the image
imagej -x 1000 -i /home/pi/CF_Images/cf_image.jpg -b /home/pi/CF_Imaging.ijm "/home/pi/CF_Images/$NAME_$DATE $TYPE"

sleep 5s

# move the processed (and unprocessed) image(s) to the synced folders
mv /home/pi/CF_Images/cf_image.jpg /home/pi/CF_Images/$NAME_$DATE.jpg
cp /home/pi/CF_Images/* $SAMBA/
mv /home/pi/CF_Images/* $RCLONE/

sleep 1s

# upload the files back to the cloud server
rclone sync -v $RCLONE/ $ONEDRIVE
