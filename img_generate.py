import argparse
import random
import os
from PIL import Image, ImageDraw, ImageFont
from preprocessing import Generator

A4_size = (1240, 1754)    # (A4 paper (150 PPI)

# parse the input arguments
parser = argparse.ArgumentParser()
parser.add_argument("--font", required=True, help="folder containing font")
parser.add_argument("--background", required=True, help="folder containing background image")
parser.add_argument("--color", required=True, help="font color")
parser.add_argument("--dictionary", required=True, help="dictionary file")
args = parser.parse_args()

# read the dictionary file
with open("dict.txt") as f:
    dictionary = f.read().splitlines()

PATH = os.getcwd()

# create the image with the specified background
background_path = os.path.join(PATH, args.background, random.choice(os.listdir(args.background)))
dictionary_path = os.path.join(PATH, args.dictionary)
generator = Generator(A4_size)

# image = Image.new("RGB", A4_size, color=(255,255,255))
image = generator.add_background(background_path, horizontal = 3)


# create a draw object and select the font
draw = ImageDraw.Draw(image)
font_path = os.path.join(PATH, args.font, random.choice(os.listdir(args.font)))
font = ImageFont.truetype(f"{font_path}", 36)

text_boxes = []
# generate the table with random characters from the dictionary
for i in range(10):
    for j in range(2):
        x = 10 + j * 1050
        y = 10 + i * 148
        text = random.choice(dictionary)
        # Draw text and save the text box
        width, height = draw.textsize(text, font=font)
        text_boxes.append((x, x + width, y, y + height))
        draw.text((x, y), text, font=font, fill=args.color)
        draw.rectangle((x, y, x + width, y + height), outline="red")

# print(text_boxes)

# save the image
image.save("image.jpg")
