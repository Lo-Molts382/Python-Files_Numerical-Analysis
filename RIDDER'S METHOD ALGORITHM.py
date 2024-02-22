# -*- coding: utf-8 -*-
"""Ridder's Method

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r2wuDIjxAwybrDbhWeWl37cu5ptuOE3Y
"""

###################################
#    RIDDER's METHOD ALGORITHM    #
###################################

import math

# Main Function
''' Declarations & Initialization/Inputs '''
a = float(input("Enter x1: "))
b = float(input("Enter x2: "))
close = float(input("Enter closeness: "))
iter = int(input("How many iterations? "))

# Function input
x = input('Enter the function: ')
exec('def f(x): return (' + x + ')')
print("\n")

res_a = f(a)
res_b = f(b)

if (res_a * res_b >= 0):
  print("\nError! f(a) * f(b) cannot be greater than or equal to 0.")

else:

  i = 0

  while True and i < iter:
    c = (a+b)/2
    res_c = f(c)
    s = math.sqrt((res_c**2)-(res_a * res_b))

    if (res_a > res_b):
        d = c + (c-a)*(res_c/s)
    elif (res_a < res_b):
        d = c - (c-a)*(res_c/s)

    res_d = f(d)
    print("Iteration [" + str(i+1) + "]:")
    print("    d = " + str(d))
    print("    res_d = " + str(res_d) + "\n")

    if (abs(res_d) < close or i == iter):
        break

    else:
        a = c
        b = d
        res_a = f(a)
        res_b = f(b)
        res_c = f(c)

    i = i + 1

  print("\n Approximate root of the eq. using Ridder's method: " + "{:.4f}".format(d))