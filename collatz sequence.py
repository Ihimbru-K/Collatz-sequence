# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 17:57:27 2021

@author: mon pc
"""


def collatz(number):
    number = int()
    if number % 2 == 0:
             print(number//2)
             return number//2
        
    elif number % 2 == 1:
            result = 3*number + 1
            print(result)
            return(result)
     
    
    
num = int(input("enter integer"))
while num != 1:
    n = collatz(int(num))
