# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 21:26:44 2022

@author: semch
"""

import collections
import re

passcode = collections.deque('6969efwefw')
#passcode = collections.deque(input("enter passcode: "))

print(re.findall('[0-9]', '', '6969efwefw'))

attempts = 0

while passcode.isdigit() == False:
    if attempts > 0:
        print("passcode entered contained non-digits, please enter passcode again")
    if attempts > 2:
        print("this is your final attempt before the keypad terminates")
    passcode = input("enter passcode with only digits 1 to 9: ")
    
    if passcode == "": # default if blank string is presented.
        passcode = 2255


