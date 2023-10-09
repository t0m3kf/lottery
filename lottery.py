#!/usr/bin/env python3
import numpy


sampleList = ["stake1", "stake2", "stake3", "stake4", "stake5"]
y = numpy.random.choice(sampleList, size=5, replace=False, p=[0.01,0.02,0.35,0.5,0.12])
print("Winner 1 = " + y[0])
print("Winner 2 = " + y[1])
print("Winner 3 = " + y[2])
print("Winner 4 = " + y[3])
print("Winner 5 = " + y[4])