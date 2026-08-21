#!/bin/bash

echo "Number1: "
read Number1
echo "Number2: "
read Number2

function maximum {
	num1=$1
	num2=$2

	if [ $num1 -gt $num2 ]; then
		echo "The maximum number is: "$num1
	elif [ $num1 -lt $num2 ]; then
		echo "The maximum number is: "$num2
	fi
}
maximum $Number1 $Number2
