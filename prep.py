from __future__ import print_function
from pprint import pprint
from collections import defaultdict, OrderedDict
import time
import json
import csv
import operator


mbta map pixels (x, y):
top left corner: (0, 0)
alewife: (987, 352)
davis: (1078, 448)
porter: (1173, 538)
harvard: (1265, 632)
central: (1359, 727)
kendall: (1450, 817)
charles/mgh: (1565, 931)
park: (1637, 1006)
downtown crossing: (1748, 1115)
south station: (1828, 1197)
broadway: (1929, 1394)
andrew: (1930, 1513)
jfk/umass: (1928, 1627)
savin hill: (1824, 1913)
fields corner: (1824, 1965)
shawmut: (1824, 2015)
ashmont: (1824, 2065)
north quincy: (2103, 1966)
wollaston: (2175, 2037)
quincy center: (2248, 2111)
quincy adams: (2300, 2187)
braintree: (2300, 2297)

bowdoin: (1643, 846)
state: (1800, 991)
aquarium: (1901, 903)
maverick: (2053, 754)
airport: (2106, 698)
wood island: (2163, 642)
orient heights: (2234, 572)
suffolk down: (2304, 501)
beachmont: (2373, 432)
revere beach: (2441, 364)
wonderland: (2525, 280)

oak grove: (1800, 178)
malden center: (1800, 250)
wellington: (1800, 323)
assembly: (1800, 393)
sullivan square: (1800, 466)
community college: (1800, 536)
north station: (1800, 710)
haymarket: (1800, 842)
state: (1800, 991)
downtown crossing: (1748, 1114)
chinatown: (1662, 1198)
tufts med center: (1516, 1346)
back bay: (1445, 1415)
mass ave: (1383, 1478)
ruggles: (1315, 1545)
roxbury crossing: (1249, 1611)
jackson sq: (1166, 1695)
stony brook: (1082, 1779)
green st: (999, 1863)
forest hills: (914, 1948)




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
