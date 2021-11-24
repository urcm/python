for root, subdirectories, files in os.walk(directory):
    for (a, subdirectory) in enumerate(subdirectories, start=1):
        path = os.path.join(root, subdirectory)
        file_counter = 1
        for filename in os.listdir(path):
            if re.search(pattern, filename):
                try:
                    os.rename(os.path.join(path, filename), path + '/' + folder_name + str(a) + '_' + 'icon' + '.png')
                    print(filename)
                except OSError as e:
                    if e.errno == errno.EEXIST:
                        print('File not renamed.')
                    else:
                        raise
            else:
                print('no match')
                try:
                    os.rename(os.path.join(path, filename), path + '/' + folder_name + str(a) + '_' + str(file_counter) + '.png')
                except OSError as e:
                    if e.errno == errno.EEXIST:
                        print('File not renamed.')
                    else:
                        raise
            file_counter += 1
