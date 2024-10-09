import random
import time
from time import perf_counter

debugCount = 0
timeStart = perf_counter()

while True:
    debugCount += 1
    insanity = float(random.randint(1, 69420727))
    penis = round(insanity / 69420727, 6)
    print("ta manane numéro " + str(penis) + " debug " + str(debugCount))
    if insanity < 2:
        timeEnd = perf_counter()
        delta = timeEnd - timeStart
        print("It took", debugCount, "iterations to find something below", str(2 / 69420727), " at a rate of", debugCount / delta, "iterations per second.", "Time elapsed:", str(delta), "seconds.")
        break
