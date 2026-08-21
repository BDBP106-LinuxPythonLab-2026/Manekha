#!/bin/bash

echo "Number1: "
read Number1
echo "Number2: "
read Number2

function divide {
	local num1=$1
	local num2=$2
	if [ "$num2" -eq 0 ]; then
		echo "Division by 0 is not possible"
		return
	fi
	local quotient=$(echo "scale=2; $num1/$num2" | bc)
	local remainder=$(echo "$num1%$num2" | bc)
	echo "Quotient: "$quotient
	echo "Remainder: "$remainder
}
divide $Number1 $Number2

