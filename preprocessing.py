from PIL import Image, ImageDraw, ImageFont
import random
import os

class Generator:
    def __init__(self, size, dictionary_path, background_path, font_path, n_row = 3, n_column = None):

        self.size = size
        self.n_row = n_row
        self.n_column = n_column
        self.image = Image.new("RGB", size, color=(255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)
        self.background_path = background_path
        self.font_path = font_path
        
        with open(dictionary_path) as f:
            self.dictionary = f.read().splitlines()

    def add_background(self, horizontal = 3, vertical = None):
       
        background = Image.open(os.path.join(self.background_path, random.choice(os.listdir(self.background_path))))
        background_width, background_height = background.size
        ratio = background_width/background_height

        width, height = self.image.size
        
        if vertical != None:
            background_height = height//vertical + 1
            background_width = int(background_height*ratio)
        else:
            background_width = width//horizontal + 1
            background_height = int(background_width/ratio)

        # Resize background, keep aspect ratio
        background = background.resize((background_width, background_height))

        # Concatenate the multiple background image and paste it to the image
        for i in range(0, height, background_height):
            for j in range(0, width, background_width):
                self.image.paste(background, (j, i))

    def add_text(self, text_size = 30, text_color = "white"):
        
        self.add_background()
        text_bboxes = []
        font_path = os.path.join(self.font_path, random.choice(os.listdir(self.font_path)))
        font = ImageFont.truetype(f"{font_path}", size = text_size)
        for i in range(10):
            for j in range(2):
                x = 10 + j * 1050
                y = 10 + i * 148
        
                text = random.choice(self.dictionary)
                # Draw text and save the text box
                width, height = self.draw.textsize(text, font=font)
                text_bboxes.append((x, x + width, y, y + height))
                self.draw.text((x, y), text, font=font, fill=text_color)
                self.draw.rectangle((x, y, x + width, y + height), outline="red")
        return self.image, text_bboxes

    


                    
