# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 05:03:02 2019

@author: aot
"""

unit1=str(input("Enter the unit of the temperature (C/K/F)="))
temp=float(input("Enter the temperature:"))

if(unit1=="K"):
    c=str(input("Enter the unit of temperature you want to convert to (C/F)="))
    if (c=="C"):
        result= temp-273.15
        print("The temperature in Celsius is ",result)
    elif (c=="F"):
        result= (temp*(9/5))-459.67
        print("The temperature in Fahrenheit is ",result)


elif(unit1=="C"):
    c=str(input("Enter the unit of temperature you want to convert to (K/F)="))
    if (c=="K"):
        result= temp+273.15
        print("The temperature in Celsius is ",result)
    elif (c=="F"):
        result= (temp*(9/5))+32
        print("The temperature in Fahrenheit is ",result)

elif(unit1=="F"):
    c=str(input("Enter the unit of temperature you want to convert to (K/C)="))
    if (c=="K"):
        result= ((temp-32)*(5/9))+273.15
        print("The temperature in Kelvin is ",result)
    elif (c=="C"):
        result= (temp-32)*(5/9)
        print("The temperature in Celsius is ",result)
else:
    print("Invalid entry, please try again !")
