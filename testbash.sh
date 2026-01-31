#!/bin/bash
echo "Who are you?"
read USER

if [ "$USER" == "User" ]; then
	echo "You are in! I'm creating your personal directory."
	mkdir -p Personal_directory
	echo "You've logged the $(date)" >> Personal_directory/Welcome.txt
else
	echo "Access denied! You're not the owner." 
	echo "$USER attempted to access $(date)" >> Attempted_access.log
fi
