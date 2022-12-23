from PIL import Image, ImageDraw

def add_background(image, background_path, horizontal = 3, vertical = None):
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

def add_text(image, font, text, text_size = 30, text_color = "white"):
    draw = ImageDraw.Draw(image)

    text_bboxes = []
    


                    
