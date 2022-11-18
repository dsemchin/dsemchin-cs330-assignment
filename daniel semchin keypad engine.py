# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 09:15:47 2022

@author: semch
"""

import unittest
import re
import collections

class state:
    def __init__(self, name, args, output):
        self.name = name
        self.args = None
        self.output = output
        self.current = False
        
    def parse(self,char):
        try:
            print(self.args(char))
            return self.args(char)
            
        except:
            return self
        
    def __repr__(self):
        return self.output
        
class fsm:
    def __init__(self):
        self.states = set({})
        self.input = None
        self.current = None
    
    def append(self, state):
        #unittest.assertIsInstance()
        self.states.add(state)
        
    def generate_states(self, passcode):
        # append lock and unlock states
        unlock_state = None
        lock_state = None
        unlock_state = state(passcode+'1',{'1':unlock_state,'4':lock_state},'UNLOCKED')
        lock_state = state(passcode+'4',{'4':lock_state,'1':unlock_state},'LOCKED')
        self.append(unlock_state)
        self.append(lock_state)
        
        # append completed passcode state
        complete_state = state(passcode,{'1':unlock_state,'4':lock_state},'NONE')
        self.append(complete_state)
        
        # append partial passcode states
        next_state = complete_state
        for i in range(len(passcode)-2,0):
            partial_state = state(passcode[0:i],{passcode[i]:next_state},'NONE')
            self.append(partial_state)
            next_state = partial_state

        # empty state
        empty_state = state('empty',{passcode[0]:next_state},'NONE')
        self.append(empty_state)
        
        # setting start state for FSM
        self.current = empty_state
        
    def find(self, name):
        return
        
    def transition(self):
        pass

    def read(self, string):
        return collections.deque(string)
    
    def run(self,passcode):
        self.generate_states(passcode)
        entry = ''
        while entry != "exit":
            entry = input("enter your passcode (enter 'exit' to quit): ")
            entry = self.read(entry)
            #print(entry)
            while entry != collections.deque([]):
                key = entry.popleft()
                self.current = self.current.parse(key)
                print(self.current.name)


passcode = input("Create a passcode (leave blank for '2255'): ")
if passcode == '':
    passcode = '2255'
    print(passcode)
keypad = fsm()
keypad.run(passcode)
          
