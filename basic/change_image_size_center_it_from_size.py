import os
from PIL import Image
from resizeimage import resizeimage


foldername = 'animal'
directory = os.path.join('D:\\wallpaper\\', foldername)

file_index = 1

for root, subdirectories, files in os.walk(directory):
    for a,file in enumerate(files):
        img_file = os.path.join(root, file)
        print(img_file)

        with open(img_file, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [1080, 1920])
                cover.save(os.path.join(root, str(file_index) +'.jpg'), image.format)

        with open(img_file, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [200, 355])
                cover.save(os.path.join(root, str(file_index) +'_t.jpg'), image.format)
                
        # delete image, we dont need it more.
        os.remove(img_file) 
        
        file_index += 1
