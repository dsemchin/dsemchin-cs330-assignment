# dsemchin-cs330-assignment
programming assignment for CS330.

## Build Instructions
These commands were tested in windows powershell\
`mkdir /tmp/daniel-semchin ; cd /tmp/daniel-semchin`\
`git clone https://github.com/dsemchin/dsemchin-cs330-assignment.git`\
`cd dsemchin-cs330-assignment`\
`.\keypad.exe`\
Otherwise, just double click on the .exe file after downloading if that doesn't work.

## How the program works

## Unit Testing Coverage
I only bring disapointment I'm afraid

## Breaking in using random number generator
### Estimating

### The actual test
I created a modified version of the main function which ran the FSM and parsed the characters. Using 
#### Code used
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
###
