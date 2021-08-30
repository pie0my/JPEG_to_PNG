from PIL import Image, ImageFilter

img = Image.open('/home/pieomy/pokemon/bulbasaur.jpg')
filtred_img = img.filter(ImageFilter.BLUR)

filtred_img.save('blurbulbasaur.png', 'png')
