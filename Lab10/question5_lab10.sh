#!/bin/bash

echo "Enter score: "
read score

if [ "$score" -ge 90 ] && [ "$score" -eq 100 ]; then
	echo "A"
elif [ "$score" -ge 80 ] && [ "$score" -le 89 ]; then
	echo "B"
elif [ "$score" -ge 70 ] && [ "$score" -le 79 ]; then
	echo "C"
else
	echo 'Fail'
fi
