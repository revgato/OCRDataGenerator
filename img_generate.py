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
generator = Generator(size = A4_size, dictionary=dictionary_path)

font_path = os.path.join(PATH, args.font, random.choice(os.listdir(args.font)))

image = generator.add_background(background_path)
image, text_boxes = generator.add_text(font_path, text_color=args.color)
# print(text_boxes)

# save the image
image.save("image.jpg")
