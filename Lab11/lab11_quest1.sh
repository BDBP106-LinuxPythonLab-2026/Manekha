#!/bin/bash

# i)
ls
ls > listoffiles
ls 1> listoffiles

ls -l . newdir
ls -l . newdir 1>presentfiles 2>filesnotpresent
#The first command long listed files in the current directory but throwed an error for 'newdir', since the directory doesnot exist.
#In the second command, the output gets stored into 'presentfiles' and the error for 'newdir' directory that doesnot exist gets stored into 'filesnotpresent'.

# ii)
ls -l . newdir >listoffiles
#The '>' operator works the same as '>1', it stores the output into 'listoffiles' but the error associated with newdir is not stored anywhere, it is displayed on the terminal itself.
