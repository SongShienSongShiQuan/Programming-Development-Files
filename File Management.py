import random
import os

if random.randint(0,6) == 1:
    
    myfile = "/Users/Chowfer/Desktop/moi.txt"
    # If file exists, delete it.
    if os.path.isfile(myfile):
        os.remove(myfile)
    else:
        # If it fails, inform the user.
        print("Error: %s file not found" % myfile)