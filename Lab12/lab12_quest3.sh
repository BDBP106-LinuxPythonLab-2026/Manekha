#!/bin/bash

echo "Input number: "
read number

i=0
until [ "$i" -eq 15 ]
do
	num=$[number*i]
	echo $num
	i=$[i+1]
done
