from PIL import Image, ImageDraw, ImageFont
import random
import os

class Generator:
    def __init__(self, size, dictionary_path, background_path, font_path):

        self.size = size
        self.image = Image.new("RGB", size, color=(255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)
        self.background_path = background_path
        self.font_path = font_path
        
        with open(dictionary_path) as f:
            self.dictionary = f.read().splitlines()

    def add_background(self, horizontal = 3, vertical = None):
       
        # Select random background
        background = Image.open(os.path.join(self.background_path, random.choice(os.listdir(self.background_path))))
        background_width, background_height = background.size

        # Resize background image, keep aspect ratio
        ratio = background_width/background_height

        width, height = self.image.size
        
        if vertical != None:
            background_height = height//vertical + 1
            background_width = int(background_height*ratio)
        else:
            background_width = width//horizontal + 1
            background_height = int(background_width/ratio)

        background = background.resize((background_width, background_height))

        # Concatenate the multiple background image and paste it to the image
        for i in range(0, height, background_height):
            for j in range(0, width, background_width):
                self.image.paste(background, (j, i))

    def add_text(self, text_size = 30, text_color = "white", margin = (20, 20), 
                 n_row = 15, n_column = 4, line_spacing = 10):
        
        # Generate image with background
        self.add_background()

        text_bboxes = []

        # Select random font
        font_path = os.path.join(self.font_path, random.choice(os.listdir(self.font_path)))
        font = ImageFont.truetype(f"{font_path}", size = text_size)

        # Calculate the max width of the text
        max_width = self.size[0]//n_column - 2*margin[0]

        # Add text to the image
        x, y = margin[0], margin[1]
        for i in range(n_row):
            for j in range(n_column):

                # Select random text
                text = random.choice(self.dictionary)

                # Crop the text if it is longer than the max width
                width, height = self.draw.textsize(text, font = font)
                char_width = width//len(text)
                if width > max_width:
                    text_length = max_width//char_width
                    text = text[:text_length]

                # Recalculate the width and height of the text
                width, height = self.draw.textsize(text, font = font)
            
                # Draw text and save the text box
                text_bboxes.append((x, x + width, y, y + height))
                self.draw.text((x, y), text, font=font, fill=text_color)
                self.draw.rectangle((x, y, x + width, y + height), outline="red")
                x = x + max_width + 2*margin[0]

            x = margin[0]    
            y = y + height + line_spacing

        return self.image, text_bboxes


    


                    
