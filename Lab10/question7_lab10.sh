#!/bin/bash
# Getting the username of the logged-in user

logged_in_user=$(whoami)

#Checking if the user is logged in

if [ -n "$logged_in_user" ]
then
	echo "The logged-in user is: "$logged_in_user
else
	echo "User is logged in"
fi

#The variable spelling was corrected from loged_in_user to logged_in_user, ')' replaced with ']' and ';' removed in line 8.
#The double quotes is shifted to position before the variable calling in line 10.
