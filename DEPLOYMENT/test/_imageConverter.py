import os
import sys
from PIL import Image
#check whether the user passed the input image or not 
if len(sys.argv) > 1:
    file =sys.argv[1]
    if os.path.exists(file):
        filename=file.split(".")
        img = Image.open(file)
        target_name = filename[0] + ".jpg"
        rgb_image = img.convert('RGB')
        rgb_image.save(target_name)
        print("Converted image saved as " + target_name)
    else:
        print(file + " not found in given location")
else:
    print("please execute the script with input image as : python tqbimageconvert.py <file>")