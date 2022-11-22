# dsemchin-cs330-assignment
author: Daniel Semchin\
A#: A20442255\
Made in python 3.9
## Build Instructions
These commands were tested in windows powershell\
`mkdir /tmp/daniel-semchin ; cd /tmp/daniel-semchin`\
`git clone https://github.com/dsemchin/dsemchin-cs330-assignment.git`\
`cd dsemchin-cs330-assignment`\
`.\keypad.exe`\
Otherwise, just double click on the .exe file after downloading if that doesn't work.

## How the program works
The following shows the FSM diagram which was implemented in my program\
![fsm-diagram](https://user-images.githubusercontent.com/118320568/203359642-0bbb987b-dd2b-4088-bf19-335dc2d17f07.png)\
Two classes were created one to represent a `state` in the FSM and then an class to create an instance of an `fsm`. The state class contained the name of a state, its output, and a dictionary which matches inputs to the next state.\
\
The `fsm` class contains all states in a list, tracks the currently active state, and parses the input strings. All inputs in the program uses regex to filter out all non-digit characters (pattern `[0-9]`). The input is read one character at a time and is passed into the current state which will check if the input exists in the dictionary. If the input exists in the state's args dictionary then the state which defines the input becomes the new current state in the fsm instance. Otherwise, if the input does not exist in the dictionary then the current state becomes an `empty state` which affectively resets the progress of the passcode. 

## Unit Testing Coverage
I only bring disapointment I'm afraid

## Breaking in using random number generator
### Estimating 
Assuming the passcode is 5 chracters long, character has a 1/10 chance of being guessed correctly. However guess them all correctly would be a (1/10)^5 chance which is 1/100000 chance of breaking in on his first try if the hacker were to systematically go through every combination (every successive attempt would have (1/(100000 - n) change, if n is the number of attempts). In total it would take 100,000 seconds (about 28 hrs to break in). However if a random number generator is used and repeats are allowed then then it can theoretically be infinite time.   
### The actual test
I created a modified version of the main function which runs the FSM and parsed the characters.
#### Code used
The following below is the code used to calculate how long it would take a hacker to break into the keypad. The passcode used was the last 5-digits of my 'A' number which are '42255'. The test was run a total of 50 times and a plot was created!

```
import matplotlib.pyplot as plt

time = []
keys = []
for i in range(50):
    time_ellapsed,keys_attempted = keypad.hack('42255')
    time.append(time_ellapsed)
    keys.append(keys_attempted)
    
plt.scatter(time,keys)
plt.title("Number of Keys Entered to Unlock vs. Time")
plt.xlabel("time (s)")
plt.ylabel("Keys Entered (1e6 keys)")
plt.show()
```
This was the resulting figure:\
![Figure](https://user-images.githubusercontent.com/118320568/203355169-608795e4-8bde-4f30-b87b-cc50d893db36.png)\
The code beneath calculated the 
```
# this prints the min, max, and average time and number of keys entered
print(min(time),max(time),sum(time)/len(time))
0.2800646000000597 30.779568800000106 11.479170805999983

print(min(keys),max(keys),sum(keys)/len(keys))
30726 3505109 1178025.02
```
Results: (time, keys entered)
* min: 0.2800646000000597s, 30726 keys
* max: 30.779568800000106s, 3505109 keys
* mean: 11.479170805999983s, 1178025.02 keys\
Much faster than expected
###
