import sys
import os
import configparser

config = configparser.ConfigParser()
config.optionxform = str

apod_conf = configparser.ConfigParser()
apod_conf.read(os.path.join('/etc','apod.conf'))

config['Unit'] = {
    'Description':'Astronomy Picture of the Day background update',
    'After':'network-online.target',
    'Wants':'network-online.target'
}
config['Service'] = {
    'Type':'forking',
    'ExecStart':(sys.executable + ' ' + os.path.join(os.getcwd(), 'APOD_wallpaper.py') + ' ' + apod_conf['DEFAULT']['api_key'])
    
}

config['Install'] = {
    'WantedBy':'multi-user.target'
}

with open(os.path.join('/lib/systemd/system', 'apod.service'), 'w') as service:
    config.write(service)
    os.chmod('/lib/systemd/system/apod.service', 0o644)