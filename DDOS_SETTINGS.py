
pause = (input("Press 'Any key to continue'..."))
input_1 = (input("Input IP Address: "))
input_2 = (input("Input your computer ACCOUNT USER NAME: "))
val_1 = str(input_1)
val_2 = str(input_2)

with open('LAN_DDOS_C#_SETTINGS.txt', 'w') as write_file:
            write_file.write(val_1)
with open('CURRENT_USER.txt', 'w') as write_file:
            write_file.write(val_2)
            with open(f'C:/Users/{val_2}/Desktop/CODE SPACE/C# WPF/Ping_C#/bin\Debug/net6.0/LAN_DDOS_C#_SETTINGS.txt', 'w') as write_file1:
                write_file1.write(val_1)