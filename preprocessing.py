from PIL import Image, ImageDraw

class Generator:
    def __init__(self, size, n_row = 3, n_column = None, dictionary):

        self.size = size
        self.n_row = n_row
        self.n_column = n_column
        self.image = Image.new("RGB", size, color=(255, 255, 255))
        self.draw = ImageDraw.Draw(image)
        
        with open(dictionary) as f:
            self.dictionary = f.read().splitlines()

    def add_background(self, background_path, horizontal = 3, vertical = None):
       
        image = self.image
        background = Image.open(background_path)
        background_width, background_height = background.size
        ratio = background_width/background_height

        width, height = image.size
        
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
                image.paste(background, (j, i))

        return image

    def add_text(self, font_path, text_size = 30, text_color = "white"):
        text_bboxes = []
        font = ImageFont.truetype(f"font_path", size = text_size)
        for i in range(10):
            for j in range(2):
                x = 10 + j * 1050
                y = 10 + i * 148
        
                text = random.choice(self.dictionary)
                # Draw text and save the text box
                width, height = self.draw.textsize(text, font=font)
                text_boxes.append((x, x + width, y, y + height))
                self.draw.text((x, y), text, font=font, fill=text_color)
                self.draw.rectangle((x, y, x + width, y + height), outline="red")
        return image, text_boxes

    


                    
