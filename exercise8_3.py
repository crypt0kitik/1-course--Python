# TASK: by using Python, create a picture
# that has an ellipse, triangle and text

# import modules for the task
from PIL import Image, ImageDraw, ImageFont

# ask an user about a color
print("1 = blue, 2 = red, 3 = yellow, 4 = green")
number = input("What number of color you want to choose? \n")
number = int(number)

# make colors as numbers
if number == 1:
    color = "blue"
elif number == 2:
    color = "red"
elif number == 3:
    color = "yellow"
elif number == 4:
    color = "green"

# create a new image, size is 100 x 30
img = Image.new('RGB', (500, 300), color=color)
# create a drawing object
d = ImageDraw.Draw(img)

# ask text from the user
text = input("Write some text:\n")


# use drawing object to draw text in the image
draw = ImageDraw.Draw(img)
I1 = ImageDraw.Draw(img)

# making a triangle and an ellipse
draw.polygon([(300, 230), (400, 50), (200, 50)], fill = (255, 255, 255))
draw.ellipse((245, 50, 355, 170), fill=(0, 0, 255))

# write text on the pic
I1.text((28, 236), text , fill=(255, 30, 0))
font = ImageFont.truetype(font='arial.ttf', size=16)
draw = ImageDraw.Draw(img)

# save image to file
img.save('test_pic.png')