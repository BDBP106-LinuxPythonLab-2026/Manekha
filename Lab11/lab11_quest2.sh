#!/bin/bash

#Use of -e:-

if [ -e "$HOME" ]; then
	echo "The variable exist."
else
	echo "The variable doesnot exist."
fi

if [ -e "$AGE" ]; then
	echo "The variable exist."
else
	echo "The variable doesnot exist."
fi

#It can check for any item regardless of whether they are files, directories etc.

#Use of -s:-

if [ -s "BrainCancer.csv" ]; then
	echo "The file exists and contains data."
else
	echo "The file doesnot exists or is empty."
fi

if [ -s "braintumor.csv" ]; then
	echo "The file exists and contains data."
else
	echo "The file doesnot exists or is empty."
fi

#It checks if a file exists and whether it conatins data. It checks for the file size to dtermine whether it has contents.

#Use of -f:-

if [ -f "BrainCancer.csv" ]; then
	echo "The file exist."
else
	echo "The file doesnot exist."
fi

if [ -f "testdir" ]; then
	echo "The file exist."
else
	echo "The file doesnot exist."
fi

#It checks if a particular file exists. It doesnot check for directories, device files etc., it only checks for regular files. 


