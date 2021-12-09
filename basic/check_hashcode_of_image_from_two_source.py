import os
import sys
import hashlib

#python ccheck_hashcode_of_image_from_two_source.py C:\Users\.. C:\Users\..
dict1 = {}

def main():
  
    directoryNew = sys.argv[1]
    directoryOld = sys.argv[2]
  
    for filename in os.listdir(directoryNew):
        fname1 = os.path.join(directoryNew, filename)
        dict1[filename] = hashlib.md5(open(fname1, 'rb').read()).hexdigest(),0     

    for filename in os.listdir(directoryOld):
        fname2 = os.path.join(directoryOld, filename)
        dict1[filename] = dict1[filename][0],hashlib.md5(open(fname2, 'rb').read()).hexdigest()    

    for filename in os.listdir(directoryOld):
        fname2 = os.path.join(directoryOld, filename)
        if dict1[filename][0] == hashlib.md5(open(fname2, 'rb').read()).hexdigest():
           print("These files have the same md5 hashcode with source")
           print(filename, dict1[filename])
           
            
if __name__ == "__main__":
    main()
