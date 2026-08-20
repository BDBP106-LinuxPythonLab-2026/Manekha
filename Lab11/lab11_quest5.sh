#!/bin/bash

# 1)
#
var1=Testing
var2=testing

# 2)
#
if [ $var1 \> $var2 ]; then
	echo "$var1 is greater than $var2"
else 
	echo "$var1 is lesser than $var2"
fi

# 3)
# The result is 'Testing is greater than testing'.


# 4)
#
echo "$var1" > teststringfile
echo "$var2" >> teststringfile

# 5)
#
sort teststringfile
# In if block, lowercase letters are greater than uppercase letter according to ASCII rule whereas in sort command, they are arranged in ascending order treating uppercase letters as greater than lowercase letters.  
