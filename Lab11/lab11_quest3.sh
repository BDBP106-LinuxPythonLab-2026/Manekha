#!/bin/bash

#The '-z' operator:

echo "Enter name: "
read name

if [ -z "$name" ]; then
	echo "Please provide your name"
else
	echo "Welcome "$name"!"
fi

#The '-n' operator:

echo "Enter name: "
read name

if [ -n "$name" ]; then
	echo "Welcome "$name"!"
else
	echo "Please provide your name"
fi
