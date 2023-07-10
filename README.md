# apod-wallpaper
## Astronomy Picture of the Day SDDM wallpaper script

apod-wallpaper uses a python script to get the NASA Astronomy Picture of the Day from a random date and uses it to set the SDDM login screen background. A shell script is used to create the necessary systemd service file, which runs on boot and edits the theme.conf file in the target sddm theme directory

## Usage
Before running the set up script, a configuration file must be created. This configuration file must be named ` apod.conf ` and must be placed in `/etc`. It has the following format:
```
[DEFAULT]
theme_directory = <path of sddm theme directory>
api_key = <NASA open api key>
```
After creating the configuration file, run
```
./setup.sh
```
