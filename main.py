#!/usr/bin/env python3

#    abc - learn order of letters in the alphabet - differently
#    Copyright (C) 2016  Matthias Krüger

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 1, or (at your option)
#    any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston MA  02110-1301 USA

import random
import sys
if (sys.version_info.major != 3): # no python 3
	print("Python 3 or higher is required.")
	sys.exit(1)

def randNumb():
	return random.randint(65,90)


def askRandChar():
	offset = random.randint(-23,23)
	charInt = randNumb()
	while (not (65 <= (charInt + offset) <= 90)): # a-z
		charInt = randNumb() # reroll

	while (1):
		offsetstr = "+" if (offset > -1) else ""
		guess = ord(input(str(chr(charInt)) +" " + offsetstr + str(offset) + " is: ").upper())
		if (guess == (charInt + offset)):
			print("correct!")
			return
		else:
			print("nope")

while(1):
	askRandChar()
