from __future__ import print_function
from pprint import pprint
from collections import defaultdict, OrderedDict
import time
import json
import csv
import operator
from operator import itemgetter
import math


# mbta map pixels (x, y):
# top left corner: (0, 0)
# alewife: (987, 352)
# davis: (1078, 448)
# porter: (1173, 538)
# harvard: (1265, 632)
# central: (1359, 727)
# kendall: (1450, 817)
# charles/mgh: (1565, 931)
# park: (1637, 1006)
# downtown crossing: (1748, 1115)
# south station: (1828, 1197)
# broadway: (1929, 1394)
# andrew: (1930, 1513)
# jfk/umass: (1928, 1627)
# savin hill: (1824, 1913)
# fields corner: (1824, 1965)
# shawmut: (1824, 2015)
# ashmont: (1824, 2065)
# north quincy: (2103, 1966)
# wollaston: (2175, 2037)
# quincy center: (2248, 2111)
# quincy adams: (2300, 2187)
# braintree: (2300, 2297)
#
# bowdoin: (1643, 846)
# state: (1800, 991)
# aquarium: (1901, 903)
# maverick: (2053, 754)
# airport: (2106, 698)
# wood island: (2163, 642)
# orient heights: (2234, 572)
# suffolk down: (2304, 501)
# beachmont: (2373, 432)
# revere beach: (2441, 364)
# wonderland: (2525, 280)
#
# oak grove: (1800, 178)
# malden center: (1800, 250)
# wellington: (1800, 323)
# assembly: (1800, 393)
# sullivan square: (1800, 466)
# community college: (1800, 536)
# north station: (1800, 710)
# haymarket: (1800, 842)
# state: (1800, 991)
# downtown crossing: (1748, 1114)
# chinatown: (1662, 1198)
# tufts med center: (1516, 1346)
# back bay: (1445, 1415)
# mass ave: (1383, 1478)
# ruggles: (1315, 1545)
# roxbury crossing: (1249, 1611)
# jackson sq: (1166, 1695)
# stony brook: (1082, 1779)
# green st: (999, 1863)
# forest hills: (914, 1948)
#
#
#
#
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

# # turn dict into a list of dicts?
# # make list of entries paired with times
# # make list of exits paired with times
# new_list = []
#
# for station in my_dict:
#     entry_list = []
#     exit_list = []
#     for date in my_dict[station]:
#         entry_item = [date, my_dict[station][date][0]]
#         exit_item = [date, my_dict[station][date][1]]
#         entry_list.append(entry_item)
#         exit_list.append(exit_item)
#     new_list.append({'station': station, 'entries': entry_list, 'exits': exit_list})
#
# with open('data_v2.json', 'wb') as fp:
#     # json.dump(my_dict, fp)
#     json.dump(new_list, fp)

for key in my_dict.keys():
    print(key)
# pprint(my_dict)

pi = math.pi

jsonCircles = [
    {
        "station": "Alewife",
        "x_axis": 987,
        "y_axis": 352,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
                    {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Davis Square",
        "x_axis": 1078,
        "y_axis": 448,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Porter Square",
        "x_axis": 1173,
        "y_axis": 538,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Harvard",
        "x_axis": 1265,
        "y_axis": 632,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Central Square",
        "x_axis": 1359,
        "y_axis": 727,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Kendall Square",
        "x_axis": 1450,
        "y_axis": 817,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Charles MGH",
        "x_axis": 1565,
        "y_axis": 931,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Park Street",
        "x_axis": 1637,
        "y_axis": 1006,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Downtown Crossing",
        "x_axis": 1748,
        "y_axis": 1115,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "South Station",
        "x_axis": 1828,
        "y_axis": 1197,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Broadway",
        "x_axis": 1929,
        "y_axis": 1394,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Andrew Square",
        "x_axis": 1930,
        "y_axis": 1513,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "JFK/U Mass",
        "x_axis": 1928,
        "y_axis": 1627,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Savin Hill",
        "x_axis": 1824,
        "y_axis": 1913,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Fields Corner",
        "x_axis": 1824,
        "y_axis": 1995,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Shawmut",
        "x_axis": 1824,
        "y_axis": 2075,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Ashmont",
        "x_axis": 1824,
        "y_axis": 2155,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "North Quincy",
        "x_axis": 2103,
        "y_axis": 1966,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Wollaston",
        "x_axis": 2175,
        "y_axis": 2037,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Quincy Center",
        "x_axis": 2248,
        "y_axis": 2111,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Quincy Adams",
        "x_axis": 2300,
        "y_axis": 2187,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Braintree",
        "x_axis": 2300,
        "y_axis": 2297,
        "color": "red",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Bowdoin",
        "x_axis": 1643,
        "y_axis": 846,
        "color": "blue",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "State Street",
        "x_axis": 1800,
        "y_axis": 991,
        "color": "blue",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Aquarium",
        "x_axis": 1901,
        "y_axis": 903,
        "color": "blue",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Maverick",
        "x_axis": 2053,
        "y_axis": 754,
        "color": "blue",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Airport",
        "x_axis": 2106,
        "y_axis": 698,
        "color": "blue",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Wood Island",
        "x_axis": 2163,
        "y_axis": 642,
        "color": "blue",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Orient Heights",
        "x_axis": 2234,
        "y_axis": 572,
        "color": "blue",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Suffolk Downs",
        "x_axis": 2304,
        "y_axis": 501,
        "color": "blue",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Beachmont",
        "x_axis": 2373,
        "y_axis": 432,
        "color": "blue",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Revere Beach",
        "x_axis": 2441,
        "y_axis": 364,
        "color": "blue",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Wonderland",
        "x_axis": 2525,
        "y_axis": 280,
        "color": "blue",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Oak Grove",
        "x_axis": 1800,
        "y_axis":178,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    # {
    #     "station": "Malden Center",
    #     "x_axis": 1800,
    #     "y_axis": 250,
    #     "color": "orange",
    #     "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
    #         {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    # },
    # {
    #     "station": "Wellington",
    #     "x_axis": 1800,
    #     "y_axis": 323,
    #     "color": "orange",
    #     "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
    #         {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    # },
    # {
    #     "station": "Assembly",
    #     "x_axis": 1800,
    #     "y_axis": 393,
    #     "color": "orange",
    #     "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
    #         {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    # },
    {
        "station": "Sullivan Square",
        "x_axis": 1800,
        "y_axis": 466,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Community College",
        "x_axis": 1800,
        "y_axis": 536,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "North Station",
        "x_axis": 1800,
        "y_axis": 710,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Haymarket",
        "x_axis": 1800,
        "y_axis": 842,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "State Street",
        "x_axis": 1800,
        "y_axis": 991,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Downtown Crossing",
        "x_axis": 1748,
        "y_axis": 1114,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Chinatown",
        "x_axis": 1662,
        "y_axis": 1198,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Tufts Medical Center",
        "x_axis": 1516,
        "y_axis": 1346,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Back Bay",
        "x_axis": 1445,
        "y_axis": 1415,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Mass Ave",
        "x_axis": 1383,
        "y_axis": 1478,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Ruggles",
        "x_axis": 1315,
        "y_axis": 1545,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Roxbury Crossing",
        "x_axis": 1249,
        "y_axis": 1611,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Jackson Square",
        "x_axis": 1166,
        "y_axis": 1695,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Stony Brook",
        "x_axis": 1082,
        "y_axis": 1779,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Green Street",
        "x_axis": 999,
        "y_axis": 1863,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    },
    {
        "station": "Forest Hills",
        "x_axis": 914,
        "y_axis": 1948,
        "color": "orange",
        "traffic": [{"startAngle": 0, "endAngle": pi, "people":20},
            {"startAngle": pi, "endAngle": 2*pi, "people":10}]
    }
]

for item in jsonCircles:
    station = item['station']
    index = map(itemgetter('station'), jsonCircles).index(station)
    print(jsonCircles[index]['traffic'][0]['people'])
    print(station)
    if 20140201 in my_dict[station]:
        print(my_dict[station][20140201])
    # jsonCircles[index]['traffic'][0]['people'] = my_dict[station][20140201][0]
    # jsonCircles[index]['traffic'][1]['people'] = my_dict[station][20140201][1]

with open('feb1.json', 'wb') as fp:
    json.dump(jsonCircles, fp)
