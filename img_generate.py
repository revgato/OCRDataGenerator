# python img_generate.py --font fonts --background images --color black --dictionary dict.txt
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
parser.add_argument("--output", default="outputs", help="output folder")
parser.add_argument("--n", default=1, help="number of images to generate")
parser.add_argument("--size", default=30, help="font size")
parser.add_argument("--column", default=2, help="number of column")
parser.add_argument("--row", default=15, help="number of row")
args = parser.parse_args()

# read the dictionary file
with open("dict.txt") as f:
    dictionary = f.read().splitlines()

PATH = os.getcwd()

# create the image with the specified background
background_path = os.path.join(PATH, args.background)
dictionary_path = os.path.join(PATH, args.dictionary)
font_path = os.path.join(PATH, args.font)
output_path = os.path.join(PATH, args.output)

generator = Generator(size = A4_size, dictionary_path=dictionary_path, background_path=background_path, font_path=font_path)


# image = generator.add_background(background_path)
image, text_boxes = generator.add_text(text_size = 30, text_color=args.color, n_column=2)
# print(text_boxes)

# save the image
image.save(os.path.join(output_path, "image1.jpg"))

image, text_boxes = generator.add_text(text_size = 100, text_color=args.color)

image.save(os.path.join(output_path, "image2.jpg"))

