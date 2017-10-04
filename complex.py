#!/usr/bin/python
#Cpurcell
#complex beginnings
def complexAdd(a, b):
    realAnswer = a[0] + b[0]
    imagAnswer = a[1] + b[1]
    return (realAnswer,imagAnswer)
print complexAdd((1,2),(3,1))
print complexAdd((0,4),(22,-6))
print complexAdd((0,4),complexAdd((22,-6),(15,-3)))

def complexSubtract(a, b):
    realAnswer = a[0] - b[0]
    imagAnswer = a[1] - b[1]
    return (realAnswer,imagAnswer)
print complexSubtract((1,2),(3,1))
print complexSubtract((0,4),(22,-6))
print complexSubtract((0,4),complexSubtract((22,-6),(15,-3)))

def complexMultiply(a, b):
    realAnswer = a[0] * b[0]
    imagAnswer = a[1] * b[1]
    return(realAnswer,imagAnswer)
print complexMultiply((1,2),(3,1))
print complexMultiply((0,4),(22,-6))
print complexMultiply((0,4),complexMultiply((22,-6),(15,-3)))

def complexDivide(a, b):
    realAnswer = a[0] / b[0]
    imagAnswer = a[1] / b[1]
    return (realAnswer,imagAnswer)
print complexDivide((1,2),(3,1))
print complexDivide((0,4),(22,-6))
print complexDivide((0,4),complexDivide((22,-6),(15,-3)))
# ComplexMath
