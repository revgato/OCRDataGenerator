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
# parser.add_argument("--color", required=True, help="font color")
parser.add_argument("--dictionary", required=True, help="dictionary file")
parser.add_argument("--output", default="outputs", help="output folder")
parser.add_argument("--n", default=1, type=int, help="number of images to generate")
parser.add_argument("--size", default=30, type=int, help="font size")
parser.add_argument("--column", default=2, type=int, help="number of column")
parser.add_argument("--row", default=15, type=int, help="number of row")
parser.add_argument("--line_spacing", default=10, type=int, help="line spacing")
parser.add_argument("--margin_x", default=20, type=int, help="margin of x")
parser.add_argument("--margin_y", default=20, type=int, help="margin of y")
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
image, text_boxes = generator.generate(text_size = args.size, n_column=args.column, n_row=args.row, 
    line_spacing=args.line_spacing, margin=(args.margin_x, args.margin_y))

# save the image
image.save(os.path.join(output_path, "image1.jpg"))

