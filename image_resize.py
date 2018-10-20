from PIL import Image

def square_the_image(image, min_size=256, fill_color=(1, 1, 1, 1)):
    x, y = image.size
    size = max(min_size, x, y)
    squared_image = Image.new('RGBA', (size, size), fill_color)
    squared_image.paste(image, ((size - x) / 2, (size - y) / 2))
    return squared_image
    
original_image = Image.open('me_rutgers.jpeg')#your imagename
squared_image = square_the_image(original_image)
squared_image.show()    