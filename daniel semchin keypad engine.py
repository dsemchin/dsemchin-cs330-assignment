# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 09:15:47 2022

@author: daniel semchin
"""

import unittest
import re
import collections

class state:
    def __init__(self, name, output):
        self.name = name
        self.args = {}
        self.output = output
        self.current = False
        
    def append_args(self, arg, next_state):
        self.args.update({arg : next_state})
        
    def parse(self,char):
        print(char)
        try: 
            #print("transition")
            return self.args.get(char)
        except:
            return self
        
    def __repr__(self):
        return str((self.name))#, self.args))
        
class fsm:
    def __init__(self):
        self.states = []
        self.input = None
        self.current = None
        
    def __repr__(self):
        return str(self.states)
    
    def append(self, state):
        self.states.append(state)
        
    def generate_states(self, passcode):
        # append lock and unlock states
        unlock_state = state(passcode+'1','UNLOCKED')
        lock_state = state(passcode+'4','LOCKED')
        
        complete_state = state(passcode,'NONE')
        complete_state.args.update({'1':unlock_state,'4':lock_state})
        print(complete_state.args)
        self.append(complete_state)
        
        # append partial passcode states
        next_state = complete_state
        for i in range(len(passcode)-1,0,-1):
            partial_state = state(passcode[0:i],'NONE')
            partial_state.args.update({passcode[i]:next_state})
            self.append(partial_state)
            next_state = partial_state

        # empty state
        empty_state = state('empty','NONE')
        empty_state.args.update({passcode[0]:next_state})
        self.append(empty_state)
        
        # setting start state for FSM
        self.current = empty_state
        print(self)
        
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
                new_state = self.current.parse(key)
                if self.current == new_state:
                    self.current = self.current
                    print('NONE')
                if type(new_state) == type(None):
                    self.current = self.states[-1]
                else:
                    self.current = new_state
                    print(self.current.output)
                print(self.current)

passcode = input("Create a passcode (leave blank for '2255'): ")
if passcode == '':
    passcode = '2255'
    print(passcode)
keypad = fsm()
keypad.run(passcode)