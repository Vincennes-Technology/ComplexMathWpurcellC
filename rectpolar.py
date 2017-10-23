#!/usr/bin/python
# Cpurcell - this is to test the complex math function (Rect to Polar and Polar to Rect)
#
import complexmath as cm
from math import *

def complexAdd(a, b):
    realAnswer = a[0] + b[0]
    imagAnswer = a[1] + b[1]
    return (realAnswer,imagAnswer)

def complexSubtract(a, b):
    realAnswer = a[0] - b[0]
    imagAnswer = a[1] - b[1]
    return (realAnswer,imagAnswer)

def complexMultiply(a, b):
    realAnswer = a[0] * b[0]
    imagAnswer = a[1] * b[1]
    return(realAnswer,imagAnswer)

def complexDivide(a, b):
    realAnswer = a[0] / b[0]
    imagAnswer = a[1] / b[1]
    return (realAnswer,imagAnswer)

def Rectangular_to_Polar(x, y):
    angle = atan((y/x))
    angle = angle * (180/pi)
    magnitude = (sqrt((x*x)+(y*y)))
    answer = magnitude, angle
    return answer

def Polar_to_Rectangular(x, y):
    y = polar_num[0] * (sin(polar_num[1] * pi/180))
    x = polar_num[0] * (cos(polar_num[1] * pi/180))
    rect = x, y
    return rect


def magnitude(number):
    absolute = sqrt((number[0] * number[0]) + (number[1]* number[1]))
    return absolute



Freq = input('What is the Freq(in Hz) = ')
voltage = input('What is the Voltage = ')
Resistor_value = input('What is the value of the Resistor = ')
Inductor= input('What kind of Inductor is in use(in Henrys) = ')
Inductor_resistance = input('What is the resistance of the Inductor coil = ')
Capacitor = input('What kind of Capacitor is in use = ')

Inductive_Reactance = 2*pi*Freq*Inductor
Capacitive_Reactance = 1/(2*pi*Freq*Capacitor)
impedance = Resistor_value, (Inductor + -Capacitor)
mag_impedance = magnitude(impedance)
current = float(voltage) / float(mag_impedance)
v_r = current * Resistor_value
v_l = current * Inductor
v_c = current * Capacitor

print('Your total impedance is: %.2f + %.2fj' % (impedance[0], impedance[1]))
print('The magnitude of your impedance is: %.2f' % mag_impedance)
print('and your current is: %f A' % current)
print('V(R) = %.2f, V(L) = %.2f, V(C) = %.2f' % (v_r, v_l, v_c))
