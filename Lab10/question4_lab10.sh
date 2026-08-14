#!/bin/bash

echo "Enter a number: "
read number

if [ "$number" -ge 0 ]; then
        if [ "$number" -eq 0 ]; then
	      echo 'The number is zero'
        else	
	      echo 'The number is positive'
        fi
else
	echo 'The number is negative'
fi


