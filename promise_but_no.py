# coding: utf-8

with open("data/temp-2021-02-02.txt", 'rb') as handle:
    data = handle.read()
    
import re

reading_regex = re.compile("(?P<timestamp>[\.\d]+)\,(?P<raw_reading>\d+)\,(?P<denoised_reading>\d+)")

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

sorted_local_maxs = sorted(local_maximum, key=lambda x:x[0])

major_maximum = set()

for previous_max_reading, this_max_reading, next_max_reading in zip(sorted_local_maxs, sorted_local_maxs[1:], sorted_local_maxs[2:]):
    if this_max_reading[1] > next_max_reading[1] and this_max_reading[1] > previous_max_reading[1]:
        major_maximum.add(this_max_reading)
        

major_maximum = set()

for previous_max_reading, this_max_reading, next_max_reading in zip(sorted_local_maxs, sorted_local_maxs[1:], sorted_local_maxs[2:]):
    if this_max_reading[1] > next_max_reading[1] or this_max_reading[1] > previous_max_reading[1]:
        major_maximum.add(this_max_reading)
        

sorted_local_mins = sorted(local_minimum, key=lambda x:x[0])

major_minimums = set()

for previous_min_reading, this_min_reading, next_min_reading in zip(sorted_local_mins, sorted_local_mins[1:], sorted_local_mins[2:]):
    if this_min_reading[1] > next_min_reading[1] or this_min_reading[1] > previous_min_reading[1]:
        major_minimums.add(this_min_reading)
        
import matplotlib.pyplot as plt

plt.title('MV Readings')

all_readings = [(idx, reading) for idx, reading in enumerate(drn)]
idxes, measurements = list(zip(*all_readings))

plt.plot(idxes, measurements, color='blue')


local = sorted(local_maximum|local_minimum, key=lambda x:x[0])

idxes, measurements = list(zip(*local))
plt.plot(idxes, measurements, color='red')

majors = sorted(major_maximum|major_minimums, key=lambda x:x[0])

idxes, measurements = list(zip(*majors))
plt.plot(idxes, measurements, color='green')

plt.show()
import matplotlib.pyplot as plt

plt.title('MV Readings')

all_readings = [(idx, reading) for idx, reading in enumerate(drn)]
idxes, measurements = list(zip(*all_readings))

plt.plot(idxes, measurements, color='blue')


local = sorted(local_maximum|local_minimum, key=lambda x:x[0])

idxes, measurements = list(zip(*local))
plt.plot(idxes, measurements, color='red')

majors = sorted(major_maximum, key=lambda x:x[0])

idxes, measurements = list(zip(*majors))
plt.plot(idxes, measurements, color='green')

plt.show()
majors = sorted(major_maximum|major_minimums, key=lambda x:x[0])

threshold = 3

general_maximums, general_minimums = set(), set()
minor_max, minor_min = set(), set()

for major1, major2, major3 in zip(majors, majors[1:], majors[2:]):
    if major1[1] > major2[1] and major2[1] < major3[1] and major1[1] - major2[1] < threshold and major3[1] - major2[1] < threshold:
        minor_min.add( major2 )
    elif major1[1] < major2[1] and major2[1] > major3[1] and abs(major1[1] - major2[1]) < threshold and abs(major3[1] - major2[1]) < threshold:
        minor_max.add( major2 )
    elif major1[1] < major2[1] and major2[1] > major3[1]:
        general_maximums.add( major2 )
    elif major1[1] > major2[1] and major2[1] < major3[1]:
        general_minimums.add( major2 )
    else:
        print(major1[1], major2[1], major3[1])
        break
            
majors = sorted(major_maximum|major_minimums, key=lambda x:x[0])

threshold = 3

general_maximums, general_minimums = set(), set()
minor_max, minor_min = set(), set()

for major1, major2, major3 in zip(majors, majors[1:], majors[2:]):
    if major1[1] >= major2[1] and major2[1] <= major3[1] and major1[1] - major2[1] < threshold and major3[1] - major2[1] < threshold:
        minor_min.add( major2 )
    elif major1[1] <= major2[1] and major2[1] >= major3[1] and abs(major1[1] - major2[1]) < threshold and abs(major3[1] - major2[1]) < threshold:
        minor_max.add( major2 )
    elif major1[1] < major2[1] and major2[1] > major3[1]:
        general_maximums.add( major2 )
    elif major1[1] > major2[1] and major2[1] < major3[1]:
        general_minimums.add( major2 )
    else:
        print(major1[1], major2[1], major3[1])
        break
            
majors = sorted(major_maximum|major_minimums, key=lambda x:x[0])

threshold = 3

general_maximums, general_minimums = set(), set()
minor_max, minor_min = set(), set()
minor_climb, minor_fall = set(), set()
general_climb, general_fall = set(), set()

for major1, major2, major3 in zip(majors, majors[1:], majors[2:]):
    if major1[1] >= major2[1] and major2[1] <= major3[1] and major1[1] - major2[1] < threshold and major3[1] - major2[1] < threshold:
        minor_min.add( major2 )
    elif major1[1] <= major2[1] and major2[1] >= major3[1] and abs(major1[1] - major2[1]) < threshold and abs(major3[1] - major2[1]) < threshold:
        minor_max.add( major2 )
    elif major1[1] < major2[1] and major2[1] > major3[1]:
        general_maximums.add( major2 )
    elif major1[1] > major2[1] and major2[1] < major3[1]:
        general_minimums.add( major2 )
    elif major1[1] > major2[1] and major2[1] > major3[1] and major1[1] - major3[1] < threshold * 2:
        minor_fall.add( major2 )
    elif major1[1] < major2[1] and major2[1] < major3[1] and major3[1] - major1[1] < threshold * 2:
        minor_climb.add( major2 )
    elif major1[1] > major2[1] and major2[1] > major3[1]:
        general_fall.add( major2 )
    elif major1[1] < major2[1] and major2[1] < major3[1]:
        general_climb.add( major2 )
    else:
        print(major1[1], major2[1], major3[1])
        break
            
majors = sorted(major_maximum|major_minimums, key=lambda x:x[0])

threshold = 3

general_maximums, general_minimums = set(), set()
minor_max, minor_min = set(), set()
minor_climb, minor_fall = set(), set()
general_climb, general_fall = set(), set()
angle_up, angle_down = set(), set()

for major1, major2, major3 in zip(majors, majors[1:], majors[2:]):
    if major1[1] >= major2[1] and major2[1] <= major3[1] and major1[1] - major2[1] < threshold and major3[1] - major2[1] < threshold:
        minor_min.add( major2 )
    elif major1[1] <= major2[1] and major2[1] >= major3[1] and abs(major1[1] - major2[1]) < threshold and abs(major3[1] - major2[1]) < threshold:
        minor_max.add( major2 )
    elif major1[1] < major2[1] and major2[1] > major3[1]:
        general_maximums.add( major2 )
    elif major1[1] > major2[1] and major2[1] < major3[1]:
        general_minimums.add( major2 )
    elif major1[1] > major2[1] and major2[1] > major3[1] and major1[1] - major3[1] < threshold * 2:
        minor_fall.add( major2 )
    elif major1[1] < major2[1] and major2[1] < major3[1] and major3[1] - major1[1] < threshold * 2:
        minor_climb.add( major2 )
    elif major1[1] > major2[1] and major2[1] > major3[1]:
        general_fall.add( major2 )
    elif major1[1] < major2[1] and major2[1] < major3[1]:
        general_climb.add( major2 )
    elif major1[1] == major2[1] and major2[1] < major3[1]:
        angle_up.add( major2 )
    elif major1[1] == major2[1] and major2[1] > major3[1]:
        angle_down.add( major2 )
    else:
        print(major1[1], major2[1], major3[1])
        break
            
majors = sorted(major_maximum|major_minimums, key=lambda x:x[0])

threshold = 3

general_maximums, general_minimums = set(), set()
minor_max, minor_min = set(), set()
minor_climb, minor_fall = set(), set()
general_climb, general_fall = set(), set()
angle_up, angle_down = set(), set()
down_flat, up_flat = set(), set()

for major1, major2, major3 in zip(majors, majors[1:], majors[2:]):
    if major1[1] >= major2[1] and major2[1] <= major3[1] and major1[1] - major2[1] < threshold and major3[1] - major2[1] < threshold:
        minor_min.add( major2 )
    elif major1[1] <= major2[1] and major2[1] >= major3[1] and abs(major1[1] - major2[1]) < threshold and abs(major3[1] - major2[1]) < threshold:
        minor_max.add( major2 )
    elif major1[1] < major2[1] and major2[1] > major3[1]:
        general_maximums.add( major2 )
    elif major1[1] > major2[1] and major2[1] < major3[1]:
        general_minimums.add( major2 )
    elif major1[1] > major2[1] and major2[1] > major3[1] and major1[1] - major3[1] < threshold * 2:
        minor_fall.add( major2 )
    elif major1[1] < major2[1] and major2[1] < major3[1] and major3[1] - major1[1] < threshold * 2:
        minor_climb.add( major2 )
    elif major1[1] > major2[1] and major2[1] > major3[1]:
        general_fall.add( major2 )
    elif major1[1] < major2[1] and major2[1] < major3[1]:
        general_climb.add( major2 )
    elif major1[1] == major2[1] and major2[1] < major3[1]:
        angle_up.add( major2 )
    elif major1[1] == major2[1] and major2[1] > major3[1]:
        angle_down.add( major2 )
    elif major1[1] > major2[1] and major2[1] == major3[1]:
        down_flat.add( major2 )
    elif major1[1] < major2[1] and major2[1] == major3[1]:
        up_flat.add( major2 )
    else:
        print(major1[1], major2[1], major3[1])
        break
            
import matplotlib.pyplot as plt

plt.title('MV Readings')

all_readings = [(idx, reading) for idx, reading in enumerate(drn)]
idxes, measurements = list(zip(*all_readings))

plt.plot(idxes, measurements, color='blue')


local = sorted(local_maximum|local_minimum, key=lambda x:x[0])

idxes, measurements = list(zip(*local))
plt.plot(idxes, measurements, color='red')

majors = sorted(major_maximum, key=lambda x:x[0])

idxes, measurements = list(zip(*majors))
plt.plot(idxes, measurements, color='green')

generals = sorted(general_climb|general_fall|general_maximums|general_minimums, key=lambda x:x[0])
idxes, measurements = list(zip(*generals))
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

majors = sorted(major_maximum, key=lambda x:x[0])

idxes, measurements = list(zip(*majors))
plt.plot(idxes, measurements, color='green')

generals = sorted(general_climb|general_fall|general_maximums|general_minimums|angle_down|angle_up|up_flat|down_flat, key=lambda x:x[0])
idxes, measurements = list(zip(*generals))
plt.plot(idxes, measurements, color='orange')

plt.show()
majors = sorted(major_maximum|major_minimums, key=lambda x:x[0])

threshold = 3

general_maximums, general_minimums = set(), set()
minor_max, minor_min = set(), set()
minor_climb, minor_fall = set(), set()
general_climb, general_fall = set(), set()
angle_up, angle_down = set(), set()
down_flat, up_flat = set(), set()

for major1, major2, major3 in zip(majors, majors[1:], majors[2:]):
    if major1[1] > major2[1] and major2[1] < major3[1] and major1[1] - major2[1] < threshold and major3[1] - major2[1] < threshold:
        minor_min.add( major2 )
    elif major1[1] < major2[1] and major2[1] > major3[1] and abs(major1[1] - major2[1]) < threshold and abs(major3[1] - major2[1]) < threshold:
        minor_max.add( major2 )
    elif major1[1] < major2[1] and major2[1] > major3[1]:
        general_maximums.add( major2 )
    elif major1[1] > major2[1] and major2[1] < major3[1]:
        general_minimums.add( major2 )
    elif major1[1] > major2[1] and major2[1] > major3[1] and major1[1] - major3[1] < threshold * 2:
        minor_fall.add( major2 )
    elif major1[1] < major2[1] and major2[1] < major3[1] and major3[1] - major1[1] < threshold * 2:
        minor_climb.add( major2 )
    elif major1[1] > major2[1] and major2[1] > major3[1]:
        general_fall.add( major2 )
    elif major1[1] < major2[1] and major2[1] < major3[1]:
        general_climb.add( major2 )
    elif major1[1] == major2[1] and major2[1] < major3[1]:
        angle_up.add( major2 )
    elif major1[1] == major2[1] and major2[1] > major3[1]:
        angle_down.add( major2 )
    elif major1[1] > major2[1] and major2[1] == major3[1]:
        down_flat.add( major2 )
    elif major1[1] < major2[1] and major2[1] == major3[1]:
        up_flat.add( major2 )
    else:
        print(major1[1], major2[1], major3[1])
        break
            
majors = sorted(major_maximum|major_minimums, key=lambda x:x[0])

threshold = 3

general_maximums, general_minimums = set(), set()
minor_max, minor_min = set(), set()
minor_climb, minor_fall = set(), set()
general_climb, general_fall = set(), set()
angle_up, angle_down = set(), set()
down_flat, up_flat = set(), set()
ignore = set()

for major1, major2, major3 in zip(majors, majors[1:], majors[2:]):
    if major1[1] > major2[1] and major2[1] < major3[1] and major1[1] - major2[1] < threshold and major3[1] - major2[1] < threshold:
        minor_min.add( major2 )
    elif major1[1] < major2[1] and major2[1] > major3[1] and abs(major1[1] - major2[1]) < threshold and abs(major3[1] - major2[1]) < threshold:
        minor_max.add( major2 )
    elif major1[1] < major2[1] and major2[1] > major3[1]:
        general_maximums.add( major2 )
    elif major1[1] > major2[1] and major2[1] < major3[1]:
        general_minimums.add( major2 )
    elif major1[1] > major2[1] and major2[1] > major3[1] and major1[1] - major3[1] < threshold * 2:
        minor_fall.add( major2 )
    elif major1[1] < major2[1] and major2[1] < major3[1] and major3[1] - major1[1] < threshold * 2:
        minor_climb.add( major2 )
    elif major1[1] > major2[1] and major2[1] > major3[1]:
        general_fall.add( major2 )
    elif major1[1] < major2[1] and major2[1] < major3[1]:
        general_climb.add( major2 )
    elif major1[1] == major2[1] and major2[1] < major3[1]:
        angle_up.add( major2 )
    elif major1[1] == major2[1] and major2[1] > major3[1]:
        angle_down.add( major2 )
    elif major1[1] > major2[1] and major2[1] == major3[1]:
        down_flat.add( major2 )
    elif major1[1] < major2[1] and major2[1] == major3[1]:
        up_flat.add( major2 )
    elif major1[1] == major2[1] and major2[1] == major3[1]:
        ignore.add( major2 )
    else:
        print(major1[1], major2[1], major3[1])
        break
import matplotlib.pyplot as plt

plt.title('MV Readings')

all_readings = [(idx, reading) for idx, reading in enumerate(drn)]
idxes, measurements = list(zip(*all_readings))

plt.plot(idxes, measurements, color='blue')


local = sorted(local_maximum|local_minimum, key=lambda x:x[0])

idxes, measurements = list(zip(*local))
plt.plot(idxes, measurements, color='red')

majors = sorted(major_maximum, key=lambda x:x[0])

idxes, measurements = list(zip(*majors))
plt.plot(idxes, measurements, color='green')

generals = sorted(general_climb|general_fall|general_maximums|general_minimums|angle_down|angle_up|up_flat|down_flat, key=lambda x:x[0])
idxes, measurements = list(zip(*generals))
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

majors = sorted(major_maximum, key=lambda x:x[0])

idxes, measurements = list(zip(*majors))
plt.plot(idxes, measurements, color='green')

generals = sorted(general_maximums|general_minimums|angle_down|angle_up|up_flat|down_flat, key=lambda x:x[0])
idxes, measurements = list(zip(*generals))
plt.plot(idxes, measurements, color='orange')

plt.show()
sorted_major_maximums = sorted(major_maximum, key=lambda x:x[0])

threshold = 3

#general_maximums, general_minimums = set(), set()
#minor_max, minor_min = set(), set()
#minor_climb, minor_fall = set(), set()
major_climb, major_fall = set(), set()
major_angle_up, major_angle_down = set(), set()
major_down_flat, major_up_flat = set(), set()
ignore = set()

for major1, major2, major3 in zip(sorted_major_maximums, sorted_major_maximums[1:], sorted_major_maximums[2:]):
    #if major1[1] > major2[1] and major2[1] < major3[1] and major1[1] - major2[1] < threshold and major3[1] - major2[1] < threshold:
    #    minor_min.add( major2 )
    #elif major1[1] < major2[1] and major2[1] > major3[1] and abs(major1[1] - major2[1]) < threshold and abs(major3[1] - major2[1]) < threshold:
    #    minor_max.add( major2 )
    #elif major1[1] < major2[1] and major2[1] > major3[1]:
    #    general_maximums.add( major2 )
    #elif major1[1] > major2[1] and major2[1] < major3[1]:
    #    general_minimums.add( major2 )
    if major1[1] > major2[1] and major2[1] > major3[1]:
        major_fall.add( major2 )
    elif major1[1] < major2[1] and major2[1] < major3[1]:
        major_climb.add( major2 )
    #elif major1[1] > major2[1] and major2[1] > major3[1]:
    #    general_fall.add( major2 )
    #elif major1[1] < major2[1] and major2[1] < major3[1]:
    #    general_climb.add( major2 )
    elif major1[1] == major2[1] and major2[1] < major3[1]:
        major_angle_up.add( major2 )
    elif major1[1] == major2[1] and major2[1] > major3[1]:
        major_angle_down.add( major2 )
    elif major1[1] > major2[1] and major2[1] == major3[1]:
        major_down_flat.add( major2 )
    elif major1[1] < major2[1] and major2[1] == major3[1]:
        major_up_flat.add( major2 )
    elif major1[1] == major2[1] and major2[1] == major3[1]:
        ignore.add( major2 )
    else:
        print(major1[1], major2[1], major3[1])
        break
    
sorted_major_maximums = sorted(major_maximum, key=lambda x:x[0])

threshold = 3

#general_maximums, general_minimums = set(), set()
#minor_max, minor_min = set(), set()
#minor_climb, minor_fall = set(), set()
major_climb, major_fall = set(), set()
major_angle_up, major_angle_down = set(), set()
major_down_flat, major_up_flat = set(), set()
ignore = set()

for major1, major2, major3 in zip(sorted_major_maximums, sorted_major_maximums[1:], sorted_major_maximums[2:]):
    #if major1[1] > major2[1] and major2[1] < major3[1] and major1[1] - major2[1] < threshold and major3[1] - major2[1] < threshold:
    #    minor_min.add( major2 )
    #elif major1[1] < major2[1] and major2[1] > major3[1] and abs(major1[1] - major2[1]) < threshold and abs(major3[1] - major2[1]) < threshold:
    #    minor_max.add( major2 )
    #elif major1[1] < major2[1] and major2[1] > major3[1]:
    #    general_maximums.add( major2 )
    #elif major1[1] > major2[1] and major2[1] < major3[1]:
    #    general_minimums.add( major2 )
    if major1[1] > major2[1] and major2[1] > major3[1]:
        major_fall.add( major2 )
    elif major1[1] < major2[1] and major2[1] < major3[1]:
        major_climb.add( major2 )
    #elif major1[1] > major2[1] and major2[1] > major3[1]:
    #    general_fall.add( major2 )
    #elif major1[1] < major2[1] and major2[1] < major3[1]:
    #    general_climb.add( major2 )
    elif major1[1] == major2[1] and major2[1] < major3[1]:
        major_angle_up.add( major2 )
    elif major1[1] == major2[1] and major2[1] > major3[1]:
        major_angle_down.add( major2 )
    elif major1[1] > major2[1] and major2[1] == major3[1]:
        major_down_flat.add( major2 )
    elif major1[1] < major2[1] and major2[1] == major3[1]:
        major_up_flat.add( major2 )
    elif major1[1] == major2[1] and major2[1] == major3[1]:
        ignore.add( major2 )
    else:
        print(major1[1], major2[1], major3[1])
        break
    
sorted_major_maximums = sorted(major_maximum, key=lambda x:x[0])

threshold = 3

#general_maximums, general_minimums = set(), set()
#minor_max, minor_min = set(), set()
#minor_climb, minor_fall = set(), set()
major_climb, major_fall = set(), set()
major_angle_up, major_angle_down = set(), set()
major_down_flat, major_up_flat = set(), set()
forgetable_max, forgetable_min = set(), set()
memorable_max, memorable_min = set(), set()
ignore = set()

for major1, major2, major3 in zip(sorted_major_maximums, sorted_major_maximums[1:], sorted_major_maximums[2:]):
    if major1[1] > major2[1] and major2[1] < major3[1] and major1[1] - major2[1] < threshold and major3[1] - major2[1] < threshold:
        forgetable_min.add( major2 )
    elif major1[1] < major2[1] and major2[1] > major3[1] and abs(major1[1] - major2[1]) < threshold and abs(major3[1] - major2[1]) < threshold:
        forgetable_max.add( major2 )
    elif major1[1] < major2[1] and major2[1] > major3[1]:
        memorable_max.add( major2 )
    elif major1[1] > major2[1] and major2[1] < major3[1]:
        memorable_min.add( major2 )
    elif major1[1] > major2[1] and major2[1] > major3[1]:
        major_fall.add( major2 )
    elif major1[1] < major2[1] and major2[1] < major3[1]:
        major_climb.add( major2 )
    #elif major1[1] > major2[1] and major2[1] > major3[1]:
    #    general_fall.add( major2 )
    #elif major1[1] < major2[1] and major2[1] < major3[1]:
    #    general_climb.add( major2 )
    elif major1[1] == major2[1] and major2[1] < major3[1]:
        major_angle_up.add( major2 )
    elif major1[1] == major2[1] and major2[1] > major3[1]:
        major_angle_down.add( major2 )
    elif major1[1] > major2[1] and major2[1] == major3[1]:
        major_down_flat.add( major2 )
    elif major1[1] < major2[1] and major2[1] == major3[1]:
        major_up_flat.add( major2 )
    elif major1[1] == major2[1] and major2[1] == major3[1]:
        ignore.add( major2 )
    else:
        print(major1[1], major2[1], major3[1])
        break
    
import matplotlib.pyplot as plt

plt.title('MV Readings')

all_readings = [(idx, reading) for idx, reading in enumerate(drn)]
idxes, measurements = list(zip(*all_readings))

plt.plot(idxes, measurements, color='blue')


local = sorted(local_maximum|local_minimum, key=lambda x:x[0])

idxes, measurements = list(zip(*local))
plt.plot(idxes, measurements, color='red')

majors = sorted(major_maximum, key=lambda x:x[0])

idxes, measurements = list(zip(*majors))
plt.plot(idxes, measurements, color='green')

generals = sorted(general_maximums|general_minimums|angle_down|angle_up|up_flat|down_flat|major_angle_down|major_angle_down|major_up_flat|major_down_flat, key=lambda x:x[0])
idxes, measurements = list(zip(*generals))
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

majors = sorted(major_maximum, key=lambda x:x[0])

idxes, measurements = list(zip(*majors))
plt.plot(idxes, measurements, color='green')

generals = sorted(general_maximums|general_minimums|angle_down|angle_up|up_flat|down_flat|major_angle_down|major_angle_down|major_up_flat|major_down_flat|forgetable_max|forgetable_min, key=lambda x:x[0])
idxes, measurements = list(zip(*generals))
plt.plot(idxes, measurements, color='orange')

plt.show()
matched_flats = set()

for gen1, gen2 in list(zip(generals, generals[1:])):
    if gen1 in angle_up and gen2 in up_flat:
        matched_flats.add(gen1)
        matched_flats.add(gen2)
    elif gen1 in major_angle_up and gen2 in up_flat:
        matched_flats.add(gen1)
        matched_flats.add(gen2)
    elif gen1 in angle_down and gen2 in down_flat:
        matched_flats.add(gen1)
        matched_flats.add(gen2)
    elif gen1 in major_angle_down and gen2 in down_flat:
        matched_flats.add(gen1)
        matched_flats.add(gen2)
        
import matplotlib.pyplot as plt

plt.title('MV Readings')

all_readings = [(idx, reading) for idx, reading in enumerate(drn)]
idxes, measurements = list(zip(*all_readings))

plt.plot(idxes, measurements, color='blue')


local = sorted(local_maximum|local_minimum, key=lambda x:x[0])

idxes, measurements = list(zip(*local))
plt.plot(idxes, measurements, color='red')

majors = sorted(major_maximum, key=lambda x:x[0])

idxes, measurements = list(zip(*majors))
plt.plot(idxes, measurements, color='green')

#generals = sorted(general_maximums|general_minimums|angle_down|angle_up|up_flat|down_flat|major_angle_down|major_angle_down|major_up_flat|major_down_flat|forgetable_max|forgetable_min, key=lambda x:x[0])
enhanced_generals = generals - matched_flats
idxes, measurements = list(zip(*generals))
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

majors = sorted(major_maximum, key=lambda x:x[0])

idxes, measurements = list(zip(*majors))
plt.plot(idxes, measurements, color='green')

#generals = sorted(general_maximums|general_minimums|angle_down|angle_up|up_flat|down_flat|major_angle_down|major_angle_down|major_up_flat|major_down_flat|forgetable_max|forgetable_min, key=lambda x:x[0])
enhanced_generals = sorted(set(generals) - matched_flats, key=lambda x:x[0])
idxes, measurements = list(zip(*generals))
plt.plot(idxes, measurements, color='orange')

plt.show()
[eg for eg in enhanced_generals if eg[0] < 907 and eg[0] > 897]
import matplotlib.pyplot as plt

plt.title('MV Readings')

all_readings = [(idx, reading) for idx, reading in enumerate(drn)]
idxes, measurements = list(zip(*all_readings))

plt.plot(idxes, measurements, color='blue')


local = sorted(local_maximum|local_minimum, key=lambda x:x[0])

idxes, measurements = list(zip(*local))
plt.plot(idxes, measurements, color='red')

majors = sorted(major_maximum, key=lambda x:x[0])

idxes, measurements = list(zip(*majors))
plt.plot(idxes, measurements, color='green')

#generals = sorted(general_maximums|general_minimums|angle_down|angle_up|up_flat|down_flat|major_angle_down|major_angle_down|major_up_flat|major_down_flat|forgetable_max|forgetable_min, key=lambda x:x[0])
enhanced_generals = sorted(set(generals) - matched_flats, key=lambda x:x[0])
idxes, measurements = list(zip(*generals))
plt.plot(idxes, measurements, color='orange')

plt.show()
[eg for eg in enhanced_generals if eg[0] < 1340 and eg[0] > 865]
get_ipython().run_line_magic('save', 'promise_but_no 0-28')
