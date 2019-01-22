import os, time, calendar

msgStr = "\
pwd-> Display the current working directory.\n\
cp-> Display all files in the current working directory.\n\
time-> Display system date time.\n\
cal-> Display the calendar of 2019-1.\n\
q-> Quit the process.\n"
cmdStr = '!q'
while(cmdStr != 'q'):
    cmdStr = input('Input an command or type "h" for help:')
    if(cmdStr == 'pwd'):
        print(os.getcwd())
    elif(cmdStr == 'cp'):
        print(os.listdir(os.getcwd()))
    elif(cmdStr == 'time'):
        print(time.asctime( time.localtime(time.time())))
    elif(cmdStr == 'cal'):
        print(calendar.month(2019, 1))
    elif(cmdStr == 'h'):
        print(msgStr)