# coding: utf-8

import re

class SegmentationDetector(object):
    """SegmentationDetector
        @path is the path to a data file to read
    """
    def __init__(self, path):
        super(SegmentationDetector, self).__init__()
        self.path = path        # "data/temp-2021-03-16.txt"
        
        self.READING_REGEX = re.compile("(?P<timestamp>[\.\d]+)\,(?P<raw_reading>\d+)\,(?P<denoised_reading>\d+)")

        self._loadReadings()

    def _readData(self):
        with open(self.path, 'rb') as handle:
            return handle.read()

    def _extractReadings(self, data):
        return [self.READING_REGEX.search(line.strip()).groupdict() for line in data.decode("utf-8").split("\n") if len(line) > 0]

    def _loadReadings(self):
        data = self._readData()
        self._readings = self._extractReadings(data)

    def getDenoisedReadings(self):
        "This method uses caching for faster results."
        if "_denoisedReadings" not in dir(self):
            self._denoisedReadings = [r['denoised_reading'] for r in self._readings]
        
        return self._denoisedReadings

    def getSmoothReadings(self, width):
        smoothed_readings = set()
        currents = list()

        for idx, reading in enumerate(self.getDenoisedReadings()):
            if len(currents) < width:
                currents.append(int(reading))
                
            if len(currents) >= width:
                smoothed_readings.add((idx, width, sum(currents)/width))
                currents.clear()
        
        return sorted(smoothed_readings, key=lambda x:x[0])

    def getDirectionalities(self, width):
        """
            Uses smoothing to calm directionality noise.
            @width - width of reading slices used in smoothing.
        """
        smoothed_readings = self.getSmoothReadings(width)

        continuations = set()
        directionality = set()

        for this_pair, next_pair in list(zip(smoothed_readings, smoothed_readings[1:])):
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

        return directionality

    def getTransitions(self, width):
        directionality = self.getDirectionalities(width)

        last_meaningful_direction = (0, "flat")
        transition_direction = (0, "flat")
        last_direction = (0, "flat")
        continuations = set()
        transitions = set()

        for dx in sorted(directionality, key=lambda x:x[0]):
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

    def getSegmentInflections(self, width):
        transitions = self.getTransitions(width)
        sorted_transitions = sorted(transitions, key=lambda x:x[0])
        
        return [(reading_index, self.getDenoisedReadings()[reading_index], direction) for reading_index, direction in sorted_transitions]





               
# len(transitions)

# import matplotlib.pyplot as plt

# plt.title('MV Readings')

# all_readings = [(idx, reading) for idx, reading in enumerate(drn)]
# idxes, measurements = list(zip(*all_readings))

# plt.plot(idxes, measurements, color='blue')


# local = sorted(local_maximum|local_minimum, key=lambda x:x[0])

# idxes, measurements = list(zip(*local))
# plt.plot(idxes, measurements, color='red')

# sorted_smoothed_readings = sorted(smoothed_readings, key=lambda x:x[0])

# idxes, _, measurements = list(zip(*sorted_smoothed_readings))
# restrung_measurements = [str(round(r)) for r in measurements]
# plt.plot(idxes, restrung_measurements, color='green')

# plt.plot(idxes, measurements, color='orange')

# plt.show()

# sorted_transitions = sorted(transitions, key=lambda x:x[0])

# idxes, _measurements = list(zip(*sorted_transitions))
# measurements = [drn[r] for r in idxes]

# len(transitions)

# [(r, drn[r], s) for r, s in sorted_transitions]
