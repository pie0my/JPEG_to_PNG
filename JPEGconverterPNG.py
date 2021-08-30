import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_image = sys.argv[2]

if not os.path.exists(output_image):
    os.makedirs(output_image)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_image}{clean_name}.png', 'png')
    print('all done')

# check if is new/exist and create new
# loop througt the pokedex
# convert images to PNG
# save to the new folder
