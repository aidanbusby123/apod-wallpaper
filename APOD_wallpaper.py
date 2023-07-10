import requests
import json
import os
import sys
from PIL import Image
import configparser
import datetime
import random

def get_data(api_key, date):
    raw_resp = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}').text
    resp = json.loads(raw_resp)
    return resp

def get_explaination(resp):
    explaination = resp['explanation']
    return explaination


def get_hdurl(resp):
    hdurl = resp['hdurl']
    return hdurl


def get_media_type(resp):
    media_type = resp['media_type']
    return media_type

def get_service_version(resp): 
    service_version = resp['service_version']
    return service_version


def get_title(resp):
    service_version = resp['title']
    return service_version

def get_url(resp):
    url = resp['url']
    return url

def get_img(url, date):
    if os.path.isfile(os.path.join('/usr/share',f'{date}.jpg')) == False:
        raw_image = requests.get(url).content
        with open(os.path.join('/usr/share',f'{date}.jpg'), 'wb') as file:
            file.write(raw_image)
            
    else:
        return FileExistsError
    
def get_apod_conf():
    config = configparser.ConfigParser()
    config.read(os.path.join('/etc', 'apod_conf'))
    return config

def random_date():
    start_dt = datetime.date(1995, 6, 16)
    end_dt = datetime.date.today()
    delta_dt = end_dt - start_dt
    delta_days = delta_dt.days
    rand_days = random.randrange(delta_days)
    rand_date = start_dt + datetime.timedelta(days=rand_days)
    return rand_date

def write_config(write_dir):
    config = configparser.ConfigParser()
    config['General'] = {'background': os.path.join('/usr/share', f'{date}.jpg')}
    with open(os.path.join(write_dir, 'theme.conf'), 'w') as configfile:
        config.write(configfile)

def wait_for_network():
    while True:
        try:
            resp = requests.get("http://www.google.com", timeout=5)
            return
        except requests.ConnectionError:
            pass


if os.path.isfile(os.path.join('/etc', 'apod_conf')):
    apod_conf = get_apod_conf()
    theme_dir = apod_conf['DEFAULT']['theme_directory']
    api_key = apod_conf['DEFAULT']['api_key']
else:
    print("Error: 'conf' does not exist. Please create one to continue")
    exit()

wait_for_network()

date = random_date()
resp = get_data(api_key, date)
url = get_hdurl(resp)
get_img(url, date)
write_config(theme_dir)
