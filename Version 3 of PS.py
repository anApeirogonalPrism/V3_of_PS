#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:23:33 2023

@author: kuro
"""

name = 'Torrez'
import math
from fractions import Fraction
from math import gcd

 

def find_gcd(x, y):
    # Find the greatest common divisor of two numbers using Euclid's algorithm
    while y:
        x, y = y, x % y
    return x

def trapezium_area(a, b, h):
    A = (a + b) / 2 * h
    return A

def say_ta(a, b, h, A, unit):
    print(f'{a}{unit} + {b}{unit} / 2 x {h}{unit} = {A}{unit}2')

def percentage_to_fraction(pn):
    # Convert the percentage to a decimal
    decimal = pn / 100
    
    # Convert the decimal to a fraction
    fraction = Fraction(decimal)
    
    return fraction

def simplify_frac(n, d):
    i = 2
    while i < min(n, d) + 1:
        if n % i == 0 and d % i == 0:
            n = n // i
            d = d // i
        else:
            i += 1
    return n, d





a = 0
b = 0
h = 0
A = 0
unit = ''

percent = '%'

dn = 0
pn = 0

fn = 0
fd = 0

n = 0
orig_n = ''
new_n = ''

x = ''
float_x = 0
i = 2





def say_ptf(pn, fn, fd):
    print(f'{pn} converted into a fraction is{fn}/{fd}')


choose = input('Choose: Area of Trapezium (aot) / conversion of DPF (cdpf)     ')
def unit_func(say_ta, a, b, h, A, unit, af_unit):
    unit += af_unit
    say_ta(a, b, h, A, unit)

def ftd():
    w = int(input('Integer? '))
    n = int(input('Numerator? '))
    d = int(input('Denominator? '))

    decimal = n / d
    integer = w
        
    num = integer + decimal
    print(f'{w} and {n}/{d} as a decimal is {num}.')

def ptd():
    percentage = float(input('Enter the percentage without the symbol: '))
    decimal = percentage / 100
    print(f'{percentage} as a decimal is {decimal}.')

def ftp():
    w = int(input('Integer? '))
    n = int(input('Numerator? '))
    d = int(input('Denominator? '))
        
    percentage = (n / d * 100) + (w * 100)
    print(percentage, '%')

if choose == 'aot':
    af_a = float(input('a?'))
    af_b = float(input('b?'))
    af_h = float(input('h'))
    a = af_a
    b = af_b
    h = af_h
    A = trapezium_area(a, b, h)
    af_unit = input('Unit? cm, mm, m etc.   ')
    if af_unit == 'mm':
        unit_func(say_ta, a, b, h, A, unit, af_unit)
    elif af_unit == 'millimetre':
        unit_func(say_ta, a, b, h, A, unit, af_unit)
    elif af_unit == 'cm':
        unit_func(say_ta, a, b, h, A, unit, af_unit)
    elif af_unit == 'centimetre':
        unit_func(say_ta, a, b, h, A, unit, af_unit)
    elif af_unit == 'm':
        unit_func(say_ta, a, b, h, A, unit, af_unit)
    elif af_unit == 'metre':
        unit_func(say_ta, a, b, h, A, unit, af_unit)
    elif af_unit == 'km':
        unit_func(say_ta, a, b, h, A, unit, af_unit)
    elif af_unit == 'kilometre':
        unit_func(say_ta, a, b, h, A, unit, af_unit)
    else:
        print('Sorry, what you entered was not a valid unit in the list. Please try again.')
elif choose == 'cdpf':
    af_base = input('How would you like to convert something? (dtp, ptf, ftd, ptd, ftp)   ')
    if af_base == 'dtp':
        decimal = float(input('Enter the decimal number: '))

        percentage = decimal * 100
        print(percent, '%')
    elif af_base == 'ptf':
        percent = float(input('Enter the percentage: '))
        decimal = percent / 100
        fraction = Fraction(decimal)
        n = fraction.numerator
        d = fraction.denominator
        while i < min(n, d) + 1:
            if n % i == 0 and d % i == 0:
                n = n // i
                d = d // i
            else:
                i += 1
        print(f'The simplest fraction form of {percent}% is {n}/{d}.')
    elif af_base == 'ftd':
        ftd()
    elif af_base == 'ptd':
        ptd()
    elif af_base == 'ftp':
        ftp()
    else:
        print('Sorry, please try something else.')