from __future__ import print_function
from pprint import pprint
from collections import defaultdict, OrderedDict
import time
import json
import csv
import operator



my_dict = defaultdict(lambda: defaultdict())
# my_dict = {"Porter": {20140201: (1,0), 20398402: (3,1), ...}, "Davis": {324:(1,3), 23451235: (3,8)}

# convert csv to json
for row in list(csv.reader(open("/Users/ashleycuster/Desktop/StationCountsByMinute_2014_02-01--03-02.csv","rb")))[1:]:
    station = row[0]
    # date = time.strptime(row[1], "%Y-%m-%d %H:%M:%S")
    year_str = row[1][0:4]
    month_str = row[1][5:7]
    day_str =  row[1][8:10]
    date = int('{}{}{}'.format(year_str, month_str, day_str))
    entries = int(row[2])
    exits = int(row[3])
    if date in my_dict[station]:
        my_dict[station][date] = tuple(map(operator.add, my_dict[station][date], (entries, exits)))
    else:
        my_dict[station][date] = (entries, exits)

# turn dict into a list of dicts?
# make list of entries paired with times
# make list of exits paired with times
new_list = []

for station in my_dict:
    entry_list = []
    exit_list = []
    for date in my_dict[station]:
        entry_item = [date, my_dict[station][date][0]]
        exit_item = [date, my_dict[station][date][1]]
        entry_list.append(entry_item)
        exit_list.append(exit_item)
    new_list.append({'station': station, 'entries': entry_list, 'exits': exit_list})

with open('data_v2.json', 'wb') as fp:
    # json.dump(my_dict, fp)
    json.dump(new_list, fp)


pprint(my_dict)

# # sort by time instead of station??
# new_list = list(defaultdict())
#
# for row in list(csv.reader(open("/Users/ashleycuster/Desktop/StationCountsByMinute_2014_02-01--03-02.csv","rb")))[1:]:
#     station = row[0]
#     # date = time.strptime(row[1], "%Y-%m-%d %H:%M:%S")
#     year_str = row[1][0:4]
#     month_str = row[1][5:7]
#     day_str =  row[1][8:10]
#     date = int('{}{}{}'.format(year_str, month_str, year_str))
#     entries = int(row[2])
#     exits = int(row[3])
#     # if the station is not yet in the list, add it to the list
#     if not any(d.get('station', None) == station for d in new_list):
#         new_list.append({"station": station, "entries":[[date,entries]], "exits":[[date,exits]]})
#     # else add time/entries/exits to dictionary
#     else:
#         new_list


# data = {
#     "Stations": [
#         {
#             "StationName": "Alewife",
#             "Traffic":[
#                 {"Time": 20140201, "Entries": 3401, "Exits": 230},
#                 {"Time": 20140201, "Entries": 3401, "Exits": 230},
#                 {"Time": 20140201, "Entries": 3401, "Exits": 230}
#             ]
#         },
#         {
#             "StationName": "Porter",
#             "Traffic":[
#                 {"Time": 20140201, "Entries": 3401, "Exits": 230},
#                 {"Time": 20140201, "Entries": 3401, "Exits": 230},
#                 {"Time": 20140201, "Entries": 3401, "Exits": 230}
#             ]
#         }
#     ]
# }
