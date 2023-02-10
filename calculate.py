from math import pi

def area(length, width, unit):
    return "The area of the house is " + str(length * width) + " square " + unit

def circumference(radius, unit):
    return "The circumference of the circle is " + str(pi * 2 * radius) + " " + unit