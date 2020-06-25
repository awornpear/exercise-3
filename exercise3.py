# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:49:52 2020

@author: Benny
"""


#Part A
def leap_year(year):
    if year % 400 ==0:
        return True
    elif  year % 4 == 0 and year % 100 != 0:
        return True
    else: 
        return False
 
#Part B
def rotate(s,n):
    if n <= len(s) and n>0:
        return s[len(s)-n:] +s[:len(s)-n]
    elif s <=1 :
        return s
    
#Part C
def digit_count(num):
    even= 0
    odd= 0
    zero= 0
    for i in str(num):
        if int(i) != '.':
            if int(i) %2 ==0 and int(i) != 0:
                even= even +1
            elif int(i) %2 != 0:
                odd= odd + 1
            else:
                zero= zero + 1
    return(even, odd, zero)

#Part D
def float_check(num):
    numdot= 0
    
    if num.isdigit():
        return True
    elif '.' in num:
        for i in range(len(num)):
            if num[i] == '.':
                numdot +=1
    else: 
        return False
            
    if numdot>1:
        return False 
    elif numdot == 1:
        return True 