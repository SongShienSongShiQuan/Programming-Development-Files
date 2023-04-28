import datetime
from logging import captureWarnings
import os
path = "C:/Users/Chowfer/Desktop/CODE SPACE/"
create_time = os.path.getmtime(path)
print(create_time)
create_date = datetime.datetime.fromtimestamp(create_time)
print('Last Modified:', create_date)


import os
import datetime

PATH = 'C:/Users/Chowfer/Desktop/CODE SPACE/'

for file in os.listdir(PATH):
    if file.endswith('.py'):
        time_get = os.path.getmtime(PATH + file)
        normalize_time = datetime.datetime.fromtimestamp(time_get)
        print(normalize_time)
pause = input("...")
        
        