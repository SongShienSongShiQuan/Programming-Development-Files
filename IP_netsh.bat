:loop
netsh int ip set address "Ethernet" static 192.168.1.15
timeout 10
goto :loop

pause