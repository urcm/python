
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
