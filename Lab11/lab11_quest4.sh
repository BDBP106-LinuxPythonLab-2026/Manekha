#!/bin/bash

val1=Jayashree
val2=Nagesh

if [ $val1 \> $val2 ]; then
	echo "$val1 is greater than $val2"
else
	echo "$val1 is lesser than $val2"
fi

# The '>' operator acts like a file redirection operator, but the '/' before '>' forces the '>' operator to act like a greater than string comparison. 
