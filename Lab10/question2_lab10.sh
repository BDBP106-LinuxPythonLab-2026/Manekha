#!/bin/bash

echo "Enter filename: "
read filename

if [ -f "$filename" ]; then
	if [ -x "$filename" ]; then
		echo 'File exists and is executable'
	else
	        echo 'File exists but is not executable'
	fi
else
	echo 'File doesnot exists'
fi        

