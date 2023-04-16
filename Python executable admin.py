import cmd
import os
import subprocess


command_prompt = 'cmd.exe'
python_executable = 'C:/Users/Chowfer/AppData/Local/Programs/Python/Python311/python.exe'
script_path = "python 'C:/Users/Chowfer/Desktop/CODE SPACE/File Management Main Admin.py' | python"


command = (script_path) #Variable set to script.


output = subprocess.run(["powershell", "-Command", command])
quit()

