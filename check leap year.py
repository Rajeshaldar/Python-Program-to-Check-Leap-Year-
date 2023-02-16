# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 21:52:13 2022

@author: Rajesh
"""

year=input('Enter a year')
i=int(year)

if(i%4==0 and i%100!=0 or i%400==0):
    print("It is a leap year")
else:
    print("It is a not leap year")