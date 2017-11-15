#!/usr/bin/python
# Cpurcell - this is to test the complex math function (Rect to Polar and Polar to Rect-parallel)
#
from math import *

# Complex math
def complexAdd(a, b):
    realAnswer = a[0] + b[0]
    imagAnswer = a[1] + b[1]
    return (realAnswer,imagAnswer)

def complexSubtract(a, b):
    realAnswer = a[0] - b[0]
    imagAnswer = a[1] - b[1]
    return (realAnswer,imagAnswer)

def complexMultiply(a, b):
    mag_Answer = a[0] * b[0]
    pha_Answer = a[1] + b[1]
    return(mag_Answer,pha_Answer)

def complexDivide(a, b):
    mag_Answer = a[0] / b[0]
    pha_Answer = a[1] - b[1]
    return (mag_Answer,pha_Answer)

def Rectangular_to_Polar(complexnumber):
    x = complexnumber[0]
    y = complexnumber[1]
    angle = atan((y/x))
    angle = angle * (180/pi)
    magnitude = (sqrt((x*x)+(y*y)))
    answer = (magnitude, angle)
    return answer

def Polar_to_Rectangular(polar_num):
    y = polar_num[0] * (sin(polar_num[1] * pi/180))
    x = polar_num[0] * (cos(polar_num[1] * pi/180))
    rect = x, y
    return rect


def magnitude(number):
    absolute = sqrt((number[0] * number[0]) + (number[1]* number[1]))
    return absolute

# Series and parallel selection.

mode_select = raw_input('Will you be doing a series or parallel circuit calculation?:')

# Series inputs.
if (mode_select == 'Series') or (mode_select == 'series'):
    Freq = float(raw_input('What is the Freq(in Hz) = '))
    voltage = float(raw_input('What is the Voltage = '))
    Resistor_value = float(raw_input('What is the value of the Resistor = '))
    Inductor= float(raw_input('What kind of Inductor is in use(in Henrys) = '))
    Inductor_resistance = float(raw_input('What is the resistance of the Inductor coil = '))
    Capacitor = float(raw_input('What kind of Capacitor is in use = '))
    
    # series calculations.
    inductive_reactance = 2 * pi * float(Freq) * float(Inductor)
    Capacitive_Reactance = 1/(2*pi*float(Freq)*float(Capacitor))
    impedance = ((float(Resistor_value) + float(Inductor_resistance)), (inductive_reactance - Capacitive_Reactance))
    #mag_impedance = magnitude(impedance)
    pol_current = complexDivide((float(voltage),0) , Rectangular_to_Polar(impedance))
    v_r = complexMultiply(pol_current , (float(Resistor_value),0))
    v_l = complexMultiply(pol_current ,(inductive_reactance,90))  
    v_c = complexMultiply(pol_current , (Capacitive_Reactance,-90))


    # Series Results.
    print "current will be: %f at a phase angle of: %f" % (pol_current[0],pol_current[1])
    print "voltage across the resistor will be: %f at a phase angle of: %f" % (v_r[0],v_r[1])
    print "voltage across the Inductor will be: %f at a phase angle of: %f" % (v_l[0],v_l[1])
    print "voltage across the Capacitor will be: %f at a phase angle of: %f" % (v_c[0],v_c[1])


# Parallel inputs.
if (mode_select == 'Parallel') or (mode_select == 'parallel'):
    Freq = float(raw_input('What is the Freq(in Hz) = '))
    voltage = float(raw_input('What is the Voltage = '))
    Resistor_value = float(raw_input('What is the value of the Resistor = '))
    Inductor= float(raw_input('What kind of Inductor is in use(in Henrys) = '))
    Inductor_resistance = float(raw_input('What is the resistance of the Inductor coil = '))
    Capacitor = float(raw_input('What kind of Capacitor is in use = '))

    # Parallel calculations.
    inductive_reactance = 2 * pi * float(Freq) * float(Inductor)
    Capacitive_Reactance = 1/(2*pi*float(Freq)*float(Capacitor))
    V = (voltage, 0)
    #impedance = ((float(Resistor_value) + float(Inductor_resistance)), (inductive_reactance - Capacitive_Reactance))
    RW = Inductor_resistance
    XL = inductive_reactance
    XC = Capacitive_Reactance
    R = Resistor_value
    Z1 = Rectangular_to_Polar((float(RW),float(XL)))
    Z2 = (float(XC),-90.0)
    Z3 = (float(R),0.0)
    one_over_Z1 = Polar_to_Rectangular(complexDivide((1,0),(Z1)))
    one_over_Z2 = Polar_to_Rectangular(complexDivide((1,0),(Z2)))
    one_over_Z3 = Polar_to_Rectangular(complexDivide((1,0),(Z3)))
    denominator = complexAdd(complexAdd(one_over_Z1,one_over_Z2),one_over_Z3)
    ZT = complexDivide((1,0),Rectangular_to_Polar(denominator))
    IC = complexDivide(V, Z1)                 
    IR = complexDivide(V, Z3)
    IL = complexDivide(V, Z2)
    IT = complexDivide(V, ZT)
                       
    # Parallel Results
    print "current through the resistor will be: %f at a phase angle of: %f" % (Z3[0],Z3[1])
    print "current through the Inductor will be: %f at a phase angle of: %f" % (Z1[0],Z1[1])
    print "current through the Capacitor will be: %f at a phase angle of: %f" % (Z2[0],Z2[1])
    print "total current will be: %f at a phase angle of: %f" % (IT[0],IT[1])
