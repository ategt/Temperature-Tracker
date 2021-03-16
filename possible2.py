# coding: utf-8

from possible import SegmentationDetector

detector = SegmentationDetector("data/temp-2021-03-04.txt", 20000)
inflection_segments = detector.getSegmentInflections(30)
detector.display(inflection_segments)
len(inflection_segments)
from possible import SegmentationDetector

detector = SegmentationDetector("data/temp-2021-02-10.txt", 20000)
inflection_segments = detector.getSegmentInflections(30)

detector.display(inflection_segments)
len(inflection_segments)
from possible import SegmentationDetector

detector = SegmentationDetector("data/temp-2021-02-10.txt", 20000)
inflection_segments = detector.getSegmentInflections(30)

detector.display(inflection_segments)
from possible import SegmentationDetector

detector = SegmentationDetector("data/temp-2021-02-10.txt", 20000)
inflection_segments = detector.getSegmentInflections(45)

detector.display(inflection_segments)
from possible import SegmentationDetector

detector = SegmentationDetector("data/temp-2021-02-10.txt", 20000)
inflection_segments = detector.getSegmentInflections(60)

detector.display(inflection_segments)
from possible import SegmentationDetector

detector = SegmentationDetector("data/temp-2021-02-10.txt", 20000)
inflection_segments = detector.getSegmentInflections(90)

detector.display(inflection_segments)
len(inflection_segments)
idxes, measurements, _directions = list(zip(*inflectionSegments))
idxes, measurements, _directions = list(zip(*inflection_segments))
def getDirectionalities(inflection_segments, width):
    """
        Uses smoothing to calm directionality noise.
        @width - width of reading slices used in smoothing.
    """
    continuations = set()
    directionality = set()

    for this_segment, next_segment in list(zip(inflection_segments, inflection_segments[1:])):
        current_idx, current_reading, current_direction = this_segment
        next_idx, next_reading, next_direction = next_segment
        
        if int(current_reading) == int(next_reading):
            directionality.add((current_idx, "flat"))
        elif int(current_reading) > int(next_reading):
            directionality.add((current_idx, "down"))
        elif int(current_reading) < int(next_reading):
            directionality.add((current_idx, "up"))
        else:
            print(current_reading, next_reading)
            break

    return directionality
def getDirectionalities(inflection_segments):
    """
        Uses smoothing to calm directionality noise.
        @width - width of reading slices used in smoothing.
    """
    continuations = set()
    directionality = set()

    for this_segment, next_segment in list(zip(inflection_segments, inflection_segments[1:])):
        current_idx, current_reading, current_direction = this_segment
        next_idx, next_reading, next_direction = next_segment
        
        if int(current_reading) == int(next_reading):
            directionality.add((current_idx, "flat"))
        elif int(current_reading) > int(next_reading):
            directionality.add((current_idx, "down"))
        elif int(current_reading) < int(next_reading):
            directionality.add((current_idx, "up"))
        else:
            print(current_reading, next_reading)
            break

    return directionality
directionalities = getDirectionalities(inflection_segments)
def getTransitions(directs):
    last_meaningful_direction = (0, "flat")
    transition_direction = (0, "flat")
    last_direction = (0, "flat")
    continuations = set()
    transitions = set()

    for dx in sorted(directs, key=lambda x:x[0]):
        if "flat" in dx:
            continuations.add(dx)
        elif last_direction[1] == dx[1]:
            continuations.add(dx)
            last_direction = dx
        elif last_direction[1] not in dx:
            last_direction = dx
            transitions.add(dx)
        else:
            print(dx, "=" * 25)
            break

    return transitions
transits = getTransitions(directionalities)
def getSegmentInflections(transitions):
    sorted_transitions = sorted(transitions, key=lambda x:x[0])
    
    return [(reading_index, self.getDenoisedReadings()[reading_index], direction) for reading_index, direction in sorted_transitions]
def getSegmentInflections(transitions, denoised_readings):
    sorted_transitions = sorted(transitions, key=lambda x:x[0])
    
    return [(reading_index, denoised_readings[reading_index], direction) for reading_index, direction in sorted_transitions]
def getDirectionalities(inflection_segments, width):
    """
        Uses smoothing to calm directionality noise.
        @width - width of reading slices used in smoothing.
    """
    continuations = set()
    directionality = set()

    for this_segment, next_segment in list(zip(inflection_segments, inflection_segments[1:])):
        current_idx, current_reading, current_direction = this_segment
        next_idx, next_reading, next_direction = next_segment
        
        if int(current_reading) == int(next_reading):
            directionality.add((current_idx, current_reading, "flat"))
        elif int(current_reading) > int(next_reading):
            directionality.add((current_idx, current_reading, "down"))
        elif int(current_reading) < int(next_reading):
            directionality.add((current_idx, current_reading, "up"))
        else:
            print(current_reading, next_reading)
            break

    return directionality
directionalities = getDirectionalities(inflection_segments)
def getDirectionalities(inflection_segments):
    """
        Uses smoothing to calm directionality noise.
        @width - width of reading slices used in smoothing.
    """
    continuations = set()
    directionality = set()

    for this_segment, next_segment in list(zip(inflection_segments, inflection_segments[1:])):
        current_idx, current_reading, current_direction = this_segment
        next_idx, next_reading, next_direction = next_segment
        
        if int(current_reading) == int(next_reading):
            directionality.add((current_idx, current_reading, "flat"))
        elif int(current_reading) > int(next_reading):
            directionality.add((current_idx, current_reading, "down"))
        elif int(current_reading) < int(next_reading):
            directionality.add((current_idx, current_reading, "up"))
        else:
            print(current_reading, next_reading)
            break

    return directionality
directionalities = getDirectionalities(inflection_segments)
def getTransitions(directs):
    last_meaningful_direction = (0, 0, "flat")
    transition_direction = (0, 0, "flat")
    last_direction = (0, 0, "flat")
    continuations = set()
    transitions = set()

    for dx in sorted(directs, key=lambda x:x[0]):
        if "flat" in dx:
            continuations.add(dx)
        elif last_direction[2] == dx[2]:
            continuations.add(dx)
            last_direction = dx
        elif last_direction[2] not in dx:
            last_direction = dx
            transitions.add(dx)
        else:
            print(dx, "=" * 25)
            break

    return transitions
transits = getTransitions(directionalities)
def getSegmentInflections(transitions):
    return sorted(transitions, key=lambda x:x[0])
reduced_segments = getSegmentInflections(transits)
len(reduced_segments)
import matplotlib.pyplot as plt

plt.title('MV Readings')

data = detector._readData()
readings = detector._extractReadings(data)

all_readings = [(idx, reading) for idx, reading in enumerate(readings)]
idxes, measurements = list(zip(*all_readings))

denoised_readings = [r['denoised_reading'] for r in measurements]

plt.plot(idxes, denoised_readings, color='blue')
idxes, measurements, _directions = list(zip(*reduced_segments))
plt.plot(idxes, measurements, color='green')
plt.show()
get_ipython().run_line_magic('save', 'possible2 0-33')
