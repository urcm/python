
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
