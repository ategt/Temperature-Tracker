# coding: utf-8

import re

reading_regex = re.compile("(?P<timestamp>[\.\d]+)\,(?P<raw_reading>\d+)\,(?P<denoised_reading>\d+)")

with open("data/temp-2021-02-02.txt", 'rb') as handle:
    data = handle.read()

readings = [reading_regex.search(line.strip()).groupdict() for line in data.decode("utf-8").split("\n") if len(line) > 0]

drn = [r['denoised_reading'] for r in readings]
import re

reading_regex = re.compile("(?P<timestamp>[\.\d]+)\,(?P<raw_reading>\d+)\,(?P<denoised_reading>\d+)")

with open("data/temp-2021-02-16.txt", 'rb') as handle:
    data = handle.read()

readings = [reading_regex.search(line.strip()).groupdict() for line in data.decode("utf-8").split("\n") if len(line) > 0]

drn = [r['denoised_reading'] for r in readings]
import re

reading_regex = re.compile("(?P<timestamp>[\.\d]+)\,(?P<raw_reading>\d+)\,(?P<denoised_reading>\d+)")

with open("data/temp-2021-03-16.txt", 'rb') as handle:
    data = handle.read()

readings = [reading_regex.search(line.strip()).groupdict() for line in data.decode("utf-8").split("\n") if len(line) > 0]

drn = [r['denoised_reading'] for r in readings]
import re

reading_regex = re.compile("(?P<timestamp>[\.\d]+)\,(?P<raw_reading>\d+)\,(?P<denoised_reading>\d+)")

with open("data/temp-2021-03-16.txt", 'rb') as handle:
    data = handle.read()

readings = [reading_regex.search(line.strip()).groupdict() for line in data.decode("utf-8").split("\n") if len(line) > 0]

drn = [r['denoised_reading'] for r in readings]

local_maximum, local_minimum = set(), set()

for idx, reading_pair in enumerate(zip(drn[1:], drn)):
    reading2, reading1 = reading_pair
    
    rdx = (idx, int(reading1))
    if reading1 != reading2 and rdx not in local_maximum | local_minimum:
        if int(reading2) < int(reading1):
            local_maximum.add(rdx)
        elif int(reading2) > int(reading1):
            local_minimum.add(rdx)
        else:
            print(rdx, reading1, reading2)
            break
smoothed_readings = set()
currents = list()

width = 60

for idx, reading in enumerate(drn):
    if len(currents) < width:
        currents.append(reading)
        
    if len(currents) >= width:
        smoothed_readings.add((idx, width, sum(currents)/width))
        currents.clear()
        
smoothed_readings = set()
currents = list()

width = 60

for idx, reading in enumerate(drn):
    if len(currents) < width:
        currents.append(int(reading))
        
    if len(currents) >= width:
        smoothed_readings.add((idx, width, sum(currents)/width))
        currents.clear()
        
len(smoothed_readings)
len(drn)
len(drn) / 60
import matplotlib.pyplot as plt

plt.title('MV Readings')

all_readings = [(idx, reading) for idx, reading in enumerate(drn)]
idxes, measurements = list(zip(*all_readings))

plt.plot(idxes, measurements, color='blue')


local = sorted(local_maximum|local_minimum, key=lambda x:x[0])

idxes, measurements = list(zip(*local))
plt.plot(idxes, measurements, color='red')

sorted_smoothed_readings = sorted(smoothed_readings, key=lambda x:x[0])

idxes, _, measurements = list(zip(*sorted_smoothed_readings))
plt.plot(idxes, measurements, color='green')

plt.show()
all_readings[25]
sorted_smoothed_readings[25]
import matplotlib.pyplot as plt

plt.title('MV Readings')

all_readings = [(idx, reading) for idx, reading in enumerate(drn)]
idxes, measurements = list(zip(*all_readings))

plt.plot(idxes, measurements, color='blue')


local = sorted(local_maximum|local_minimum, key=lambda x:x[0])

idxes, measurements = list(zip(*local))
plt.plot(idxes, measurements, color='red')

sorted_smoothed_readings = sorted(smoothed_readings, key=lambda x:x[0])

idxes, _, measurements = list(zip(*sorted_smoothed_readings))
restrung_measurements = [str(round(r)) for r in measurements]
plt.plot(idxes, restrung_measurements, color='green')

plt.show()
smoothed_readings = set()
currents = list()

width = 30

for idx, reading in enumerate(drn):
    if len(currents) < width:
        currents.append(int(reading))
        
    if len(currents) >= width:
        smoothed_readings.add((idx, width, sum(currents)/width))
        currents.clear()
        
import matplotlib.pyplot as plt

plt.title('MV Readings')

all_readings = [(idx, reading) for idx, reading in enumerate(drn)]
idxes, measurements = list(zip(*all_readings))

plt.plot(idxes, measurements, color='blue')


local = sorted(local_maximum|local_minimum, key=lambda x:x[0])

idxes, measurements = list(zip(*local))
plt.plot(idxes, measurements, color='red')

sorted_smoothed_readings = sorted(smoothed_readings, key=lambda x:x[0])

idxes, _, measurements = list(zip(*sorted_smoothed_readings))
restrung_measurements = [str(round(r)) for r in measurements]
plt.plot(idxes, restrung_measurements, color='green')

plt.show()
transitions = set()
continuations = set()
directionality = set()

for this_pair, next_pair in list(zip(sorted_smoothed_readings, sorted_smoothed_readings[1:])):
    current_idx, current_width, current_reading = this_pair
    next_idx, next_width, next_reading = next_pair
    
    if int(current_reading) == int(next_reading):
        directionality.add((current_idx, "flat"))
    elif int(current_reading) > int(next_reading):
        directionality.add((current_idx, "down"))
    elif int(current_reading) < int(next_reading):
        directionality.add((current_idx, "up"))
    else:
        print(current_reading, next_reading)
        break
    
last_meaningful_direction = (0, "flat")

for dx in directionality:
    if last_meaningful_direction[1] == dx[1] or last_meaningful_direction[1] == "flat":
        continuations.add(dx)
    elif last_meaningful_direction[1] != "flat" and last_meaningful_direction[1] != dx[1]:
        transitions.add(dx)
    else:
        print(dx)
        break
            
len(transitions)
last_meaningful_direction = (0, "flat")

for dx in sorted(directionality, key=lambda x:x[0]):
    if last_meaningful_direction[1] == dx[1] or last_meaningful_direction[1] == "flat":
        continuations.add(dx)
    elif last_meaningful_direction[1] != "flat" and last_meaningful_direction[1] != dx[1]:
        transitions.add(dx)
    else:
        print(dx)
        break
            
len(transitions)
len(continuations)
len(drn) / 60
len(smoothed_readings)
sorted(directionality, key=lambda x:x[0])[5]
sorted(directionality, key=lambda x:x[0])[26]
last_meaningful_direction = (0, "flat")

for dx in sorted(directionality, key=lambda x:x[0]):
    if last_meaningful_direction[1] == dx[1]:
        print(dx, same)
        continuations.add(dx)
    elif "flat" in last_meaningful_direction:
        print(dx, "flat)
        continuations.add(dx)
    elif last_meaningful_direction[1] not in dx:
        print(dx, last_meaningful_direction, "change")
        transitions.add(dx)
    else:
        print(dx, "=" * 25)
        break
            
last_meaningful_direction = (0, "flat")

for dx in sorted(directionality, key=lambda x:x[0]):
    if last_meaningful_direction[1] == dx[1]:
        print(dx, same)
        continuations.add(dx)
    elif "flat" in last_meaningful_direction:
        print(dx, "flat")
        continuations.add(dx)
    elif last_meaningful_direction[1] not in dx:
        print(dx, last_meaningful_direction, "change")
        transitions.add(dx)
    else:
        print(dx, "=" * 25)
        break
            
last_meaningful_direction = (0, "flat")

for dx in sorted(directionality, key=lambda x:x[0]):
    if last_meaningful_direction[1] == dx[1]:
        print(dx, "same")
        continuations.add(dx)
    elif "flat" in last_meaningful_direction:
        print(dx, "flat")
        continuations.add(dx)
    elif last_meaningful_direction[1] not in dx:
        print(dx, last_meaningful_direction, "change")
        transitions.add(dx)
    else:
        print(dx, "=" * 25)
        break
            
last_meaningful_direction = (0, "flat")
transition_direction = (0, "flat")
last_direction = (0, "flat")

for dx in sorted(directionality, key=lambda x:x[0]):
    if "flat" in dx:
        #print(dx, "flat")
        continuations.add(dx)
    elif last_direction[1] == dx[1]:
        #print(dx, "same")
        continuations.add(dx)
        last_direction = dx
    elif last_direction[1] not in dx:
        #print(dx, last_meaningful_direction, "change")
        transitions.add(dx)
    else:
        print(dx, "=" * 25)
        break
               
len(transitions)
last_meaningful_direction = (0, "flat")
transition_direction = (0, "flat")
last_direction = (0, "flat")
transitions = set()

for dx in sorted(directionality, key=lambda x:x[0]):
    if "flat" in dx:
        #print(dx, "flat")
        continuations.add(dx)
    elif last_direction[1] == dx[1]:
        #print(dx, "same")
        continuations.add(dx)
        last_direction = dx
    elif last_direction[1] not in dx:
        #print(dx, last_meaningful_direction, "change")
        last_direction = dx
        transitions.add(dx)
    else:
        print(dx, "=" * 25)
        break
               
len(transitions)
import matplotlib.pyplot as plt

plt.title('MV Readings')

all_readings = [(idx, reading) for idx, reading in enumerate(drn)]
idxes, measurements = list(zip(*all_readings))

plt.plot(idxes, measurements, color='blue')


local = sorted(local_maximum|local_minimum, key=lambda x:x[0])

idxes, measurements = list(zip(*local))
plt.plot(idxes, measurements, color='red')

sorted_smoothed_readings = sorted(smoothed_readings, key=lambda x:x[0])

idxes, _, measurements = list(zip(*sorted_smoothed_readings))
restrung_measurements = [str(round(r)) for r in measurements]
plt.plot(idxes, restrung_measurements, color='green')

sorted_transitions = sorted(transitions, key=lambda x:x[0])

idxes, measurements = list(zip(*sorted_transitions))
plt.plot(idxes, measurements, color='orange')

plt.show()
import matplotlib.pyplot as plt

plt.title('MV Readings')

all_readings = [(idx, reading) for idx, reading in enumerate(drn)]
idxes, measurements = list(zip(*all_readings))

plt.plot(idxes, measurements, color='blue')


local = sorted(local_maximum|local_minimum, key=lambda x:x[0])

idxes, measurements = list(zip(*local))
plt.plot(idxes, measurements, color='red')

sorted_smoothed_readings = sorted(smoothed_readings, key=lambda x:x[0])

idxes, _, measurements = list(zip(*sorted_smoothed_readings))
restrung_measurements = [str(round(r)) for r in measurements]
plt.plot(idxes, restrung_measurements, color='green')

sorted_transitions = sorted(transitions, key=lambda x:x[0])

idxes, _measurements = list(zip(*sorted_transitions))
measurements = [drn[r] for r in idxes]
plt.plot(idxes, measurements, color='orange')

plt.show()
len(transitions)
[(r, drn[r]) for r in idxes]
[(r, drn[r], s) for r, s in sorted_transitions]
get_ipython().run_line_magic('save', 'possible 0-38')
