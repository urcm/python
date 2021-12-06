
for root, subdirectories, files in os.walk(directory):
    for (a, subdirectory) in enumerate(subdirectories, start=1):
        path = os.path.join(root, subdirectory)
        list = os.listdir(path)
        number_files = len(list)
        arry = []
        new_im = Image.new('RGB', (800, 800))
        for filename in list:
            file = os.path.join(path, filename)
            if re.search('_icon', file):
                pass
            else:
                arry.append(file)
                
        images = []
        for x in arry:
            images.append(Image.open(x))
        widths, heights = zip(*(i.size for i in images))

        total_width = sum(widths)
        max_height = max(heights)

        new_im = Image.new('RGB', (total_width, max_height))
        
        x_offset = 0
        for im in images:
            new_im.paste(im, (x_offset, 0))
            x_offset += im.size[0]

        im_pth = os.path.join(directory, subdirectory + '.jpg')
        new_im.save(im_pth)
        
        image = Image.open(im_pth)
        new_image = image.resize(((int(total_width / 2), int(max(heights) / 2))))
        new_image.save(im_pth)
    
