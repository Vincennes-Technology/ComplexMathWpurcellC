#!/usr/bin/python
# Cpurcell - this is to test the complex math function
#
import complexmath as cm

response1 = raw_input("are you using Rectangular notation (R) or Polar (P)")
response2 = raw_input("First number (x,y) :")
numberstrings = response2.split(',')
numberx = float(numberstrings[0][1:])
numbery = float(numberstrings[1][:-1])
print numberx
print numbery
