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
    date = int('{}{}{}'.format(year_str, month_str, year_str))
    entries = int(row[2])
    exits = int(row[3])
    if date in my_dict[station]:
        my_dict[station][date] = tuple(map(operator.add, my_dict[station][date], (entries, exits)))
    else:
        my_dict[station][date] = (entries, exits)

pprint(my_dict)

data = {
    "Stations": [
        {
            "StationName": "Alewife",
            "Traffic":[
                {"Time": 20140201, "Entries": 3401, "Exits": 230},
                {"Time": 20140201, "Entries": 3401, "Exits": 230},
                {"Time": 20140201, "Entries": 3401, "Exits": 230}
            ]
        },
        {
            "StationName": "Porter",
            "Traffic":[
                {"Time": 20140201, "Entries": 3401, "Exits": 230},
                {"Time": 20140201, "Entries": 3401, "Exits": 230},
                {"Time": 20140201, "Entries": 3401, "Exits": 230}
            ]
        }
    ]
}
