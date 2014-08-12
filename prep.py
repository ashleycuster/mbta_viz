from __future__ import print_function
from pprint import pprint
from collections import defaultdict, OrderedDict
import time
import json
import csv
import operator
from operator import itemgetter
import math


my_dict = defaultdict(lambda: defaultdict())
# my_dict = {"Porter": {20140201: (1,0), 20398402: (3,1), ...}, "Davis": {324:(1,3), 23451235: (3,8)}

# convert csv to json
for row in list(csv.reader(open("/Users/ashleycuster/Desktop/StationCountsByMinute_2014_02-01--03-02.csv","rb")))[1:]:
    station = row[0]
    # date = time.strptime(row[1], "%Y-%m-%d %H:%M:%S")
    year_str = row[1][0:4]
    month_str = row[1][5:7]
    day_str =  row[1][8:10]
    hour_str = row[1][11:13]
    date = int('{}{}{}{}'.format(year_str, month_str, day_str, hour_str))
    entries = int(row[2])
    exits = int(row[3])
    if date in my_dict[station]:
        my_dict[station][date] = tuple(map(operator.add, my_dict[station][date], (entries, exits)))
    else:
        my_dict[station][date] = (entries, exits)

jsonData = list(defaultdict())

# get all the times from one station, e.g. Park
# use this list of times as times to append
# in for loop, check for existance of time in my_dict[station]
#    if present, do the same thing (append)
#    else, append a made up value... but what? 0 for now, see how that looks

time_list = []
for time in my_dict["Park Street"]:
    time_list.append(time)
time_list.sort()

# num_people = [[time, num_people], [time, num_people], ...]

for station in my_dict:
    num_entries = []
    num_exits = []
    for time in time_list:
        if time in my_dict[station]:
            entry = my_dict[station][time][0]
            exit = my_dict[station][time][1]
        else:
            entry = 0
            exit = 0
        num_entries.append([ time, entry ])
        num_exits.append([ time, exit ])
    jsonData.append({'station': station, 'direction': 'entry', 'num_people': sorted(num_entries)})
    jsonData.append({'station': station, 'direction': 'exit', 'num_people': sorted(num_exits)})

# for station in my_dict:
#     num_entries = []
#     num_exits = []
#     for time in my_dict[station]:
#         num_entries.append([ time, my_dict[station][time][0] ])
#         num_exits.append([ time, my_dict[station][time][1] ])
#     jsonData.append({'station': station, 'direction': 'entry', 'num_people': sorted(num_entries)})
#     jsonData.append({'station': station, 'direction': 'exit', 'num_people': sorted(num_exits)})

with open('allfeb_hourly_v2.js', 'wb') as fp:
    fp.write('var traffic_data = ')
    json.dump(jsonData, fp)
