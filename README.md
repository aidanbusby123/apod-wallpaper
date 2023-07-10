# apod-wallpaper
## Astronomy Picture of the Day SDDM wallpaper script

apod-wallpaper uses a python script to get the NASA Astronomy Picture of the Day from a random date and uses it to set the SDDM login screen background. A shell script is used to create the necessary systemd service file, which runs on boot and edits the theme.conf file in the target sddm theme directory

## Use
To set up the program to run on boot, run
```
./setup.sh
```
