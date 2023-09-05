# U14553-Zakee

## Introduction

## Prerequisites

#python install embedded on raspberry PI

$ pip3 install pyembedded

# this code must be used to install Raspbian spidev depending on the version as the Python pre-installed packages are not included 

python adc.py

## Installation 

## Other

## Contributors

System Script

#redirects script output into logging_script and onto a file named log_file

import sys
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', '%m-%d-%Y %H:%M:%S')

stdout_handler = logging,StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)
 
file_handler = logging.FileHandler('log_file')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
 
logger.addHandler(file_handler)
logger.addHandler(stdout_handler)

#setting up of the camera to enable taking pictures
 
#!/usr/bin/env python3
 
# [START includes]
from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont
from datetime import datetime
import os
 
def write_timestamps(font_large,font_small,output_folder):
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_large)
    fontsmall = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_small)
    fontcolor = (51, 102, 255)
    counter = 0
    for i in os.listdir(output_folder):
        if i.endswitch(".jpg"):
            counter += 1
            img = Image.open(output_folder+'/'+ i)
            date_captured_str = img._getexif()[36867]
            date_captured = datetime.strptime(date_captured_str, "%Y:%m:%d %H:%M:%S")
            date = date_captured.strftime('%Y-%m-%d')
            t = date_captured.strftime('%H:%M:S')
 
            # Adding colon to time
 
            tformatted = t[o:2] + ":" + t[3:5] + ':' + t[6:8]
            # Open image and resize to HD format
            widthtarget = 1920
            heighttarget = 1080
            downSampleRatio = float(widthtarget) / float(img.width)
            imgDownSampled = img.resize( (widthtarget,round(img.height*downSampleRatio) ), resample=Image.LANCXOS)
            imgDownSampled = imgDownSampled.crop((0,180,widthtarget, heighttarget+180))
            # get a drawing context
 
            draw = ImageDraw.Draw(imgDownSampled)
            draw.text((imgDownSampled.width-250,imgDownSampled.height-130), date, fontcolor, font=fontsmall)
            draw.text((imgDownSampled.width-350,imgDownSampled.height-100), tformatted, fontcolor, font=font)
            filename = output_folder + '/' + i[0:-4] + "-resized.jpg"
            imgDownSampled.save(filename)
 
 
Log Rotation Script
rotateLogs () {
    SIZE=$ (WC -1     |   awk '{print}')
    COUNT_LOG_FILES=$ (ls      |   grep    ".*.gz"   |   wc -1)
    echo    
    if  [[   -gt 1500 ]]; then
    mv .1.gz .2.gz || continue # if ! exist ignore logger "ace:rotateLogs" "rotating log shifting by 1"
    gzip -c  > .1.gz
    resetlog
    fi
 
System Management
#BASH being used to print out temp and current CPU frequency 
 
#pi@raspberrypi:~ $ cat ./cpu_freq.sh
#!/bin/bash
 
temp='head -n 1 /sys/class/thermal/thermal_zone0/temp   |   xargs -I{} awk "BEGIN {printf\"%.2f\n\", {}/1000}"'
 
echo $(('cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq'/1000)) MHz,  degrees
 
# the monitor interval: every 5 seconds
while : ; do ./cpu_freq.sh; sleep 5; done
 

#IP address management
 
import struct 
import socket
import fcntl 
 
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,     #SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
 
    get_ip_address('eth0')
 
# get CPU usage, disk space used and available and RAM info
 
from pyembedded.raspberry_pi_tools.raspberrypi import PI
 
pi = PI()
 
print(pi.get_ram_info())
print(pi.get_disk_space())
print(pi.get_cpu_usage())
 
# get status of wifi
 
print(pi.get_connected_ip_addr(network='wlan0'))
print(pi.get_wifi_status())
 
# get current user

import os 
os.environ.get('USERNAME')

# get hostname
 
import socket
print (socket.gethostname())
 
#display device voltage
 
import time
import spidev 
 
spi_ch = 0
 
#Allow SPI
spi = spidev.SpiDev(0, spi_ch)
spi.max_speed_hz = 1200000
 
def read_adc(adc_ch, vref = 3,3):
 
    # Check to see ADC channel is 0 or 1
    if adc_ch != 0:
        adc_ch = 1
 
        #Build SPI message
                
        #   First bit (Start); Logic high (1)
                
        #   Second bit (SGL/DIFF): 1 to select single mode
                
        #   Third bit (ODD/SIGN): Select channel (0 or 1)
                
        #   Fourth bit (MSFB): 0 for LSB first
        #   Next 12 bits: 0
 
        msg = 0b11
        msg = ((msg << 1) + adc_ch) << 5
        msg = [,msg 0b00000000]
        reply = spi.xfer2(msg)
 
        #Build single integer using the reply (2 bytes)
 
        adc = 0
        for n in reply:
            adc = (adc << 8) + n
       
        adc = adc >> 1
 
        #Work out voltage using ADC value
 
        voltage = (vref * adc) / 1024
 
        return voltage
 
#Present voltages for channel 0 and channel 1  to the terminal
 
try:
    while True:
        adc_0 = read_adc(0)
        adc_1 = read_adc(1)
        print("Ch 0:", round(adc_0, 2), "V Ch 1:", round(adc_1, 2), "V")
        time.sleep(0.2)
 
finally:
    spi.close()
    GPIO.cleanup()
