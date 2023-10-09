#!/usr/bin/env python3
import numpy
import json
import requests
import sys
import re
from sklearn import preprocessing

#delegators_api_url = "https://api.koios.rest/api/v0/pool_delegators?_pool_bech32=pool19xyfanyp28j6j07dxgwdjp0wur6seqmyyu64qgzstzl7s47pvpj&select=stake_address,amount,active_epoch_no&order=active_epoch_no"
#epoch_api_url = "https://api.koios.rest/api/v0/tip?select=epoch_no"
#response = requests.get(api_url)
#curr_epoch = response.json()[0]['epoch_no']
#print ("Current epoch number: " + str(curr_epoch))


filename = sys.argv[1]
file_epoch = re.findall(r'\d+', filename)
print("Lottery epoch: " + file_epoch[0])
file = open(filename)
delegators_list = json.load(file)

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

#------------convert list of ADA amount from strings to intigers
amounts = list(map(int, amounts))
print("Total stake = " + str(sum(amounts)/1000000) + "\n")
#amounts = numpy.array(amounts, dtype=int)

#------------extract number of active epochs per delegator
active_epochs = []
for i in delegators_list:
    active_epochs.append(int(file_epoch[0])-i['active_epoch_no'])

#------------normalize values of 'tickets' for numpy.random function
weights = [float(i)/sum(amounts) for i in amounts]
#print(sum(weights))

#------------choose 5 stake keys with no repetition using amount of stake as 'weights'
winners = numpy.random.choice(stake_keys, size=5, replace=False, p=weights)
print("Winner 1 = " + winners[0])
print("Winner 2 = " + winners[1])
print("Winner 3 = " + winners[2])
print("Winner 4 = " + winners[3])
print("Winner 5 = " + winners[4])
