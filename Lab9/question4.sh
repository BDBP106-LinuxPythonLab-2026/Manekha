#!/bin/bash

echo $?

date ; echo $0

echo 'The first argument is: '$1
echo 'The second argument is: '$2

echo 'The number of arguments passed on this script: '$#
echo 'The array/list of arguments passed to this script: '$@

# We can store the arguments in an array by entering $@ within()
listofarg=($@)
#Recall elements like any other array
echo ${listofarg[2]}

