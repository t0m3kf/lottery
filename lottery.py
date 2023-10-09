#!/usr/bin/env python3
import numpy
import json
import random

file = open("epoch_441.json")
delegators_list = json.load(file)

#print(delegators_list[1]['stake_address'])

#-------------loop through the JSON and extract stake keys, save as python list
stake_keys = []
for i in delegators_list:
    #print(i['stake_address'])
    stake_keys.append(i['stake_address'])
#print(len(stake_keys))

#-------------loop through the JSON and extract ADA stake amount, save as python list
amounts = []
for i in delegators_list:
    amounts.append(i['amount'])
#print(amounts[1])
#------------convert list of strings to intiger
amounts = list(map(int, amounts))
#amounts = numpy.array(amounts, dtype=int)


#stake_keys = ["stake1", "stake2", "stake3", "stake4", "stake5"]
y = random.choices(stake_keys, weights = amounts, k=5)
#y = numpy.random.choice(stake_keys, size=5, replace=False, p=[amount])
print("Winner 1 = " + y[0])
print("Winner 2 = " + y[1])
print("Winner 3 = " + y[2])
print("Winner 4 = " + y[3])
print("Winner 5 = " + y[4])


