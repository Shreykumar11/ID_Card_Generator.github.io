import random
import os
import datetime
import pyqrcode
import png
import PIL

from PIL import Image, ImageDraw, ImageFont
from pyqrcode import QRCode

image = Image.new('RGB', (1200, 900), (255, 255, 255))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=45)

os.system("Title: ID CARD Generator by Grasp Coding")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
print( '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(reg_format_date)
print( '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# starting position of the message
(x, y) = (50, 50)
message = input('\nEnter Your Company Name: ')
company = message
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial.ttf', size=80)
draw.text((x, y), message, fill=color, font=font)

# adding an unique id number. You can manually take it from user
(x, y) = (750, 180)
idno = random.randint(10000000, 90000000)
message = str('ID: ' + str(idno))
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 250)
message = input('Enter Your Full Name: ')
name = message
message = str('Name: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 350)
message = input('Enter Your Gender: ')
message = str('Gender: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (400, 350)
message = int(input('Enter Your Age: '))
message = str('Age: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 450)
message = input('Enter Your Date Of Birth: ')
message = str('Date of Birth: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 550)
message = input('Enter Your Blood Group: ')
message = str('Blood Group: ' + str(message))
color = 'rgb(255, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 650)
message = int(input('Enter Your Mobile Number: '))
temp = message
message = str('Mobile Number: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 750)
message = input('Enter Your Address: ')
message = str('Address: ' + str(message))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), message, fill=color, font=font)

# save the edited image

image.save(str(name) + '.png')

img = pyqrcode.create(str(company) + str(idno))  # this info. is added in QR code, also add other things
img.svg(str(idno)+'.svg', scale = 8)
img.png(str(idno)+'.png', scale = 6)

til = Image.open(str(idno) + '.png')
image.paste(til, (800, 400)) # 25x25
image.save(name + '.png')

print(('\n\n\nYour ID Card Successfully created in a PNG file ' + name + '.png'))
input('\n\nPress ENTER key to Close program...')
