#!/usr/bin/env python3
from termcolor import colored # pip3 install termcolor
import datetime as dt
import sys
from time import sleep
import argparse

lastCheckpoint = "/var/log/timePeek_lastCheckpointTime.txt"

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

def getTimeElapsed(lastCheckpoint, now):
	#with open(lastCheckpoint, 'r'):
	#return deltablabla
	print("Here I would print you a calculation of how much time has passed since the last evocation")

def main():
	# Gather the arguments
	parser = argparse.ArgumentParser(description='-=- Run with either no arguments or --mode')
	parser.add_argument("--mode", nargs='?')
	args = parser.parse_args()

	# Print the date
	sys.stdout.write(">>> ")
	printWithStyle("hour")
	printWithStyle("date")

	# Maybe print a calculation of time has passed since the last evocation 
	if args.mode == "log":
		print(getTimeElapsed(lastCheckpoint,dt.datetime.now()))

	# Hide screen after glimpsed
	sleep(2)
	clearScreen()

if __name__ == "__main__":
	main()