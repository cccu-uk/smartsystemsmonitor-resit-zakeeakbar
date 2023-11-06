#!/usr/bin/env python3
 
#setting up of the camera to enable taking pictures
 
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
