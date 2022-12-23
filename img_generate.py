# python img_generate.py --font ../fonts/ko --background ../TextRecognitionDataGenerator/trdg/images/ --color black --dictionary dict.txt
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
background_path = os.path.join(PATH, args.background)
dictionary_path = os.path.join(PATH, args.dictionary)
font_path = os.path.join(PATH, args.font)

generator = Generator(size = A4_size, dictionary_path=dictionary_path, background_path=background_path, font_path=font_path)


# image = generator.add_background(background_path)
image, text_boxes = generator.add_text(text_size = 100, text_color=args.color)
# print(text_boxes)

# save the image
image.save("image.jpg")

image, text_boxes = generator.add_text(text_color=args.color)

image.save("image2.jpg")

