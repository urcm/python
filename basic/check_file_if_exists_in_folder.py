
directory = 'F:\'

folderlistfull, folderlistfiles  = [], []
for root, subdirectories, files in os.walk(directory):
    for (a, subdirectory) in enumerate(subdirectories, start=1):
        path = os.path.join(root, subdirectory)
        folderlistfull.append(path)
        list = os.listdir(path)
        for filename in list:
            file = os.path.join(path, filename)
            if re.search('_icon', file):
                folderlistfiles.append(path)
            else:
                pass

folder_diff = set(folderlistfull).difference(set(folderlistfiles))
