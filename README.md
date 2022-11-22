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
Assuming the passcode is 5 chracters long, character has a 1/10 chance of being guessed correctly. However guess them all correctly would be a (1/10)^5 chance which
### The actual test
I created a modified version of the main function which ran the FSM and parsed the characters. Using 
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
[Figure](https://user-images.githubusercontent.com/118320568/203351430-a579f433-f493-4290-9e6b-c1a02a9c76e7.png)
The code beneath calculated the 
```
# this prints the min, max, and average time and number of keys entered
print(min(time),max(time),sum(time)/len(time))
0.2800646000000597 30.779568800000106 11.479170805999983

print(min(keys),max(keys),sum(keys)/len(keys))
30726 3505109 1178025.02
```
###
