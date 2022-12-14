import unittest
import re
import collections
import sys
import random
import timeit

    # Class object contains name of state, input args defined by a dictionary,
    # and outputs a string
class state:
    def __init__(self, name, output):
        self.name = name
        self.args = {}
        self.output = str(output)
        
    def __repr__(self):
        return str((self.name))
        
    def append_args(self, arg, next_state):
        self.args.update({arg : next_state})
    
    def set_output(self, output):
        self.output = output
    
    def parse(self,char):
        try: 
            return self.args.get(char)
        except:
            return self
        

class fsm:
    def __init__(self):
        self.states = []
        self.input = None
        self.current = None
        
    def __repr__(self):
        return str(self.states)
    
        # appends a state to list of states in FSM instance.
    def append(self, state):
        self.states.append(state)
        
        # creates states and relations between each digit in passcode and 
        # states for locking and unlocking. 
    def generate_states(self, passcode):
        # append lock and unlock states
        unlock_state = state(passcode+'1','UNLOCKED')
        lock_state = state(passcode+'4','LOCKED')
        
        self.append(unlock_state)
        self.append(lock_state)
        
        self.states[0].append_args('1', unlock_state)
        self.states[0].append_args('4', lock_state)
        self.states[1].append_args('1', unlock_state)
        self.states[1].append_args('4', lock_state)
            
        # append complete passcode state
        complete_state = state(passcode,'NONE')
        complete_state.args.update({'1':unlock_state,'4':lock_state})
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

    def read(self, string):
        return collections.deque(string)
    
    def run(self):
        passcode = input("Create a passcode (leave blank for '42255'), non-digits are ignored: ")
        passcode = ''.join(re.findall('[0-9]', passcode))
        if passcode == '':
            passcode = '42255'
            print(passcode)
        self.generate_states(passcode)
        entry = ''
        while entry != "end":
            entry = input("enter your passcode (enter 'end' to quit): ")
            if entry == 'end':
                sys.exit("program terminated")
            entry = ''.join(re.findall('[0-9]', entry))
            entry = self.read(entry)
            while entry != collections.deque([]):
                key = entry.popleft()
                new_state = self.current.parse(key)
                
                if type(new_state) == type(None):
                    self.current = self.states[-1]
                    print("Parsed: " + str(key))
                    print("Output: " + str(self.current.output))
                    print(" State: " + str(self.current))
                    
                elif self.current != new_state:
                    self.current.out = new_state.output
                    self.current = new_state    
                    print("Parsed: " + str(key))
                    print("Output: " + str(self.current.output))
                    print(" State: " + str(self.current))
                    
                elif self.current == new_state:
                    original = self.current.output
                    new_state.set_output('NONE')
                    print("Parsed: " + str(key))
                    print("Output: " + str(new_state.output))
                    print(" State: " + str(self.current))
                    self.current.set_output(original)
                    self.current = self.current
                    
    def hack(self,passcode):
        self.generate_states(passcode)
        start_time = timeit.default_timer()
        keys_attempted = 0
        while self.current.output != "UNLOCKED":
            entry = str(random.randint(0,9))
            if self.current.output == 'UNLOCKED':
                sys.exit("program terminated")
            entry = self.read(entry)
            while entry != collections.deque([]):
                key = entry.popleft()
                keys_attempted += 1
                new_state = self.current.parse(key)
                
                if type(new_state) == type(None):
                    self.current = self.states[-1]
                    print("Parsed: " + str(key))
                    print("Output: " + str(self.current.output))
                    print(" State: " + str(self.current))
                    
                elif self.current != new_state:
                    self.current.out = new_state.output
                    self.current = new_state    
                    print("Parsed: " + str(key))
                    print("Output: " + str(self.current.output))
                    print(" State: " + str(self.current))
                    
                elif self.current == new_state:
                    original = self.current.output
                    new_state.set_output('NONE')
                    print("Parsed: " + str(key))
                    print("Output: " + str(new_state.output))
                    print(" State: " + str(self.current))
                    self.current.set_output(original)
                    self.current = self.current
        time_ellapsed = timeit.default_timer() - start_time        
        print(time_ellapsed)
        print(keys_attempted)
        return (time_ellapsed,keys_attempted) 


keypad = fsm()
keypad.run()

# import matplotlib.pyplot as plt

# time = []
# keys = []
# for i in range(50):
#     time_ellapsed,keys_attempted = keypad.hack('42255')
#     time.append(time_ellapsed)
#     keys.append(keys_attempted)
    
# plt.scatter(time,keys)
# plt.title("Number of Keys Entered to Unlock vs. Time")
# plt.xlabel("time (s)")
# plt.ylabel("Keys Entered (1e6 keys)")
# plt.show()

    










