#!/usr/bin/env python3
from termcolor import colored # pip3 install termcolor
import datetime as dt
import sys
from time import sleep

def printHour(color):
	sys.stdout.write(">>> ")
	now = dt.datetime.now()
	print(colored("%0.2d:%0.2d" % (now.hour, now.minute), color))

def clearScreen():
	'''Clears screen'''
	print("\033[H\033[J")

printHour("cyan")
sleep(2)
clearScreen()