# TASK: generate wallpaper with
# random phrases from internet data

# import modules
import json
import requests
import var_dump as vd
from PIL import Image, ImageDraw, ImageFont
from colorama import Fore, Back, Style

# data from the Internet
url = "https://api.adviceslip.com/advice"
req = requests.get(url)
data = req.json()

# ask data from user
user_data = input(Back.BLUE + "Do you feel tired and frustrated? (y/n): \n")
user_data = user_data.lower()

# if a user wants to run the application
if user_data == "y":
    print("I have something for you :)")
    print("Below you can find a wallpaper that could motivate you <3")
    print()

    # get a phrase from data
    phrase = data['slip']['advice']

    # create an image with this phrase
    # create a new image, size is 900 x 600
    img = Image.new('RGB', (900, 600), color=(255, 192, 203))
    # create a drawing object
    d = ImageDraw.Draw(img)
    # use drawing object to draw text in the image
    d.text((100, 300), phrase, fill=(255, 255, 255))
    # save image to file
    img.save('motivation_wallpaper.png')

# if a user doesn't want to run the application
else:
    print("Well, in this case bye-bye!")
