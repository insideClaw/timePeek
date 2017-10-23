#!/usr/bin/env python3
from termcolor import colored # pip3 install termcolor
import datetime as dt
import sys
from time import sleep

def printWithStyle(mode):
	'''Defines style and prints when called for an hour/date'''
	now = dt.datetime.now()
	if mode == "hour":
		print(colored("%0.2d:%0.2d" % (now.hour, now.minute), "cyan"))
	elif mode == "date":
		print(colored("    %d/%d/%d" % (now.day, now.month, now.year), "green", attrs=['dark']))

def clearScreen():
	'''Clears screen'''
	print("\033[H\033[J")

sys.stdout.write(">>> ")
printWithStyle("hour")
printWithStyle("date")
sleep(2)
clearScreen()