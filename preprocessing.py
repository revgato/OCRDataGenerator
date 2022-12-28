from PIL import Image, ImageDraw, ImageFont
import random
import os
import numpy as np

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

    def generate(self, output_folder, n = 1, text_size = 30, margin = (20, 20),
                 n_row = 15, n_column = 4, line_spacing = 10):
        
        output_folder = self.check_output_folder_name(output_folder)
        for k in range(n):
            with open(os.path.join(output_folder, f"image{k}.txt"), "w") as f:
                # Generate image with background
                self.add_background()

                # text_bboxes = []          # Uncomment this line if you want to return the text box

                # Select random font
                font_path = os.path.join(self.font_path, random.choice(os.listdir(self.font_path)))
                font = ImageFont.truetype(f"{font_path}", size = text_size)

                # Calculate the max width of the text
                max_width = self.size[0]//n_column - 2*margin[0]
                # max_height = self.size[1]//n_row - 2*margin[1] - line_spacing//2

                # Add text to the image
                x, y = margin[0], margin[1]

                # Estimating color of text
                color = self.color_estimation()
                # color = 'black'

                for i in range(n_row):
                    for j in range(n_column):

                        # Select random text
                        text = random.choice(self.dictionary)

                        # Write text to the file

                        # Crop the text if it is longer than the max width
                        width, height = self.draw.textsize(text, font = font)
                        char_width = width//len(text)
                        if width > max_width:
                            text_length = max_width//char_width
                            text = text[:text_length]
                        
                        f.write(text + "\n")

                        # Recalculate the width and height of the text
                        # width, height = self.draw.textsize(text, font = font)       # Uncomment this line if you want to return the text box
                    
                        # Draw text and save the text box
                        # text_bboxes.append((x, x + width, y, y + height))         # Uncomment this line if you want to return the text box
                        self.draw.text((x, y), text, font=font, fill=color)
                        # self.draw.rectangle((x, y, x + width, y + height), outline="red")         # Uncomment this line if you want to return the text box
                        x = x + max_width + 2*margin[0]

                    x = margin[0]    
                    # y = y + max_height + line_spacing
                    y = y + height + line_spacing


                    # If the text is out of the image, break the loop
                    if y > self.size[1]:
                        break
                
                self.image.save(os.path.join(output_folder, f"image{k}.png"))
                print(f"Generated {k+1}/{n} images")

        # return self.image, text_bboxes

    def color_estimation(self):

        # Convert the image to numpy array
        image = np.array(self.image)

        # Get the average color of the image
        r, g, b = image.mean(axis=0).mean(axis=0)
        r, g, b = int(r), int(g), int(b)
        
        # Return the opposite color of the average color
        return (255 - r, 255 - g, 255 - b)

    def check_output_folder_name(self, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            return output_folder
        
        i = 1
        while(os.path.exists(f"{output_folder}{i}")):
            i += 1
        os.makedirs(f"{output_folder}{i}")
        return f"{output_folder}{i}"



    


                    
