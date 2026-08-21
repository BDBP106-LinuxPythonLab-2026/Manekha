#!/bin/bash

echo "Enter directory name: "
read dir_name

function directory {
	dir=$1
	if [ -d "$dir" ]; then
		echo "The directory exists"
		ls $dir
	else
		echo "The directory doesn't exists"
		mkdir $dir
	fi
}
directory $dir_name
