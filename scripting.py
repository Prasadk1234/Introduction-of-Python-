from PIL import Image, ImageFilter

img = Image.open("C:\\Users\\LENOVO\\Downloads\\pexels-oleksandr-pidvalnyi-1093230.jpg")

img.thumbnail((400,400))
img.save('tHUmbnail.jpg')
