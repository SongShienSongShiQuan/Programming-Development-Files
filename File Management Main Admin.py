import os
import ctypes, sys

myfile = "/Users/Chowfer/Desktop/moi.txt"

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return True

if is_admin():
    if  os.path.isfile(myfile):
        os.remove(myfile)
        print("File has been deleted 1")
    else:
        # If it fails, inform the user.
        print("Error: %s file not found" % myfile)
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1, os.remove(myfile))
    print("File has been deleted 2")
