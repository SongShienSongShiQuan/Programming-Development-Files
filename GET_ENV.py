import subprocess
import os

def SAVE_ENV_Function():
        try:
            executecommand = 'set PATH'
            command = executecommand
            output2 = subprocess.run(command, capture_output=True, shell=True).stdout
            output2length = output2.decode("utf-8")
            print('OUTPUT:', output2length)
        except Exception as error_output:
            print('Error Function Loc>sec_a0056:', error_output)
SAVE_ENV_Function()