#! /usr/bin/python3

# This program will take inputs specifying the
# microwave power you have, the microwave power that
# the foot item is suggesting and the time the packet
# says to cook for in minutes and in seconds.
# The program will then calculate how long you should
# adjust cooking times for.

# Import modules

import argparse
import time
import os

# Clear the terminal to give a fresh screen.
os.system('cls' if os.name == 'nt' else 'clear')

# Initiate the argument parser and specify the
# accepted arguments.

parser = argparse.ArgumentParser(
    prog="mwc",
    description='Microwave Wattage Converter',
    epilog=
    "Welcome to the microwave wattage calculator, use this to enter in your settings and let the program calculate how long you should cook for."
)
parser.add_argument('--yourmic',
                    action="store",
                    help='Enter your microwave Wattage.',
                    required=True,
                    type=int)
parser.add_argument('--othermic',
                    action="store",
                    help='Enter the packaging microwave wattage.',
                    required=True,
                    type=int)
parser.add_argument('--min',
                    action="store",
                    help='Enter the time in minutes on the packaging.',
                    required=True,
                    type=int)
parser.add_argument('--sec',
                    action="store",
                    help='Enter the time in seconds on the packaging',
                    required=True,
                    type=int)

args = parser.parse_args()

# Assign the arguments to these variables for
# using in the program (Probably don't need to do this)

yr_microwave = int(args.yourmic)
fd_microwave = int(args.othermic)
time_min = int(args.min)
time_sec = int(args.sec)


def calculateWatt(yr_microwave, fd_microwave, time_min, time_sec):

    #convert minutes into seconds
    min_to_sec = time_min * 60

    #Add minutes and seconds together.
    total_time = min_to_sec + time_sec

    #Do the calculation and print the time out.
    result = fd_microwave / yr_microwave * total_time

    sec = result
    ty_res = time.gmtime(sec)
    res = time.strftime("%M:%S", ty_res)
    print(f"You need to cook for {res}")


calculateWatt(yr_microwave, fd_microwave, time_min, time_sec)
