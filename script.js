// # mbta map pixels (x, y):
// # top left corner: (0, 0)
// # alewife: (987, 352)
// # davis: (1078, 448)
// # porter: (1173, 538)
// # harvard: (1265, 632)
// # central: (1359, 727)
// # kendall: (1450, 817)
// # charles/mgh: (1565, 931)
// # park: (1637, 1006)
// # downtown crossing: (1748, 1115)
// # south station: (1828, 1197)
// # broadway: (1929, 1394)
// # andrew: (1930, 1513)
// # jfk/umass: (1928, 1627)
// # savin hill: (1824, 1913)
// # fields corner: (1824, 1965)
// # shawmut: (1824, 2015)
// # ashmont: (1824, 2065)
// # north quincy: (2103, 1966)
// # wollaston: (2175, 2037)
// # quincy center: (2248, 2111)
// # quincy adams: (2300, 2187)
// # braintree: (2300, 2297)
// #
// # bowdoin: (1643, 846)
// # state: (1800, 991)
// # aquarium: (1901, 903)
// # maverick: (2053, 754)
// # airport: (2106, 698)
// # wood island: (2163, 642)
// # orient heights: (2234, 572)
// # suffolk down: (2304, 501)
// # beachmont: (2373, 432)
// # revere beach: (2441, 364)
// # wonderland: (2525, 280)
// #
// # oak grove: (1800, 178)
// # malden center: (1800, 250)
// # wellington: (1800, 323)
// # assembly: (1800, 393)
// # sullivan square: (1800, 466)
// # community college: (1800, 536)
// # north station: (1800, 710)
// # haymarket: (1800, 842)
// # state: (1800, 991)
// # downtown crossing: (1748, 1114)
// # chinatown: (1662, 1198)
// # tufts med center: (1516, 1346)
// # back bay: (1445, 1415)
// # mass ave: (1383, 1478)
// # ruggles: (1315, 1545)
// # roxbury crossing: (1249, 1611)
// # jackson sq: (1166, 1695)
// # stony brook: (1082, 1779)
// # green st: (999, 1863)
// # forest hills: (914, 1948)
// #
// #



var jsonCircles = [{"color": "red", "y_axis": 352, "x_axis": 987, "station": "Alewife", "traffic": [{"endAngle": 3.141592653589793, "people": 4604, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 4511, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 448, "x_axis": 1078, "station": "Davis Square", "traffic": [{"endAngle": 3.141592653589793, "people": 9151, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 5502, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 538, "x_axis": 1173, "station": "Porter Square", "traffic": [{"endAngle": 3.141592653589793, "people": 5422, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 5142, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 632, "x_axis": 1265, "station": "Harvard", "traffic": [{"endAngle": 3.141592653589793, "people": 17129, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 16781, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 727, "x_axis": 1359, "station": "Central Square", "traffic": [{"endAngle": 3.141592653589793, "people": 10552, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 10658, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 817, "x_axis": 1450, "station": "Kendall Square", "traffic": [{"endAngle": 3.141592653589793, "people": 6335, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 5382, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 931, "x_axis": 1565, "station": "Charles MGH", "traffic": [{"endAngle": 3.141592653589793, "people": 4398, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 3450, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 1006, "x_axis": 1637, "station": "Park Street", "traffic": [{"endAngle": 3.141592653589793, "people": 10434, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 10064, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 1115, "x_axis": 1748, "station": "Downtown Crossing", "traffic": [{"endAngle": 3.141592653589793, "people": 9422, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 7650, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 1197, "x_axis": 1828, "station": "South Station", "traffic": [{"endAngle": 3.141592653589793, "people": 7783, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 5627, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 1394, "x_axis": 1929, "station": "Broadway", "traffic": [{"endAngle": 3.141592653589793, "people": 2732, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 2898, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 1513, "x_axis": 1930, "station": "Andrew Square", "traffic": [{"endAngle": 3.141592653589793, "people": 3498, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 1281, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 1627, "x_axis": 1928, "station": "JFK/U Mass", "traffic": [{"endAngle": 3.141592653589793, "people": 4031, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 2516, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 1913, "x_axis": 1824, "station": "Savin Hill", "traffic": [{"endAngle": 3.141592653589793, "people": 1306, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 1290, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 1995, "x_axis": 1824, "station": "Fields Corner", "traffic": [{"endAngle": 3.141592653589793, "people": 2971, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 2712, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 2075, "x_axis": 1824, "station": "Shawmut", "traffic": [{"endAngle": 3.141592653589793, "people": 1160, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 600, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 2155, "x_axis": 1824, "station": "Ashmont", "traffic": [{"endAngle": 3.141592653589793, "people": 4442, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 344, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 1966, "x_axis": 2103, "station": "North Quincy", "traffic": [{"endAngle": 3.141592653589793, "people": 2549, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 2304, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 2037, "x_axis": 2175, "station": "Wollaston", "traffic": [{"endAngle": 3.141592653589793, "people": 2334, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 2043, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 2111, "x_axis": 2248, "station": "Quincy Center", "traffic": [{"endAngle": 3.141592653589793, "people": 3833, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 4136, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 2187, "x_axis": 2300, "station": "Quincy Adams", "traffic": [{"endAngle": 3.141592653589793, "people": 1747, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 742, "startAngle": 3.141592653589793}]},
                    {"color": "red", "y_axis": 2297, "x_axis": 2300, "station": "Braintree", "traffic": [{"endAngle": 3.141592653589793, "people": 2218, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 1226, "startAngle": 3.141592653589793}]},
                    {"color": "blue", "y_axis": 846, "x_axis": 1643, "station": "Bowdoin", "traffic": [{"endAngle": 3.141592653589793, "people": 258, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 236, "startAngle": 3.141592653589793}]},
                    {"color": "blue", "y_axis": 991, "x_axis": 1800, "station": "State Street", "traffic": [{"endAngle": 3.141592653589793, "people": 3969, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 4591, "startAngle": 3.141592653589793}]},
                    {"color": "blue", "y_axis": 903, "x_axis": 1901, "station": "Aquarium", "traffic": [{"endAngle": 3.141592653589793, "people": 3067, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 2355, "startAngle": 3.141592653589793}]},
                    {"color": "blue", "y_axis": 754, "x_axis": 2053, "station": "Maverick", "traffic": [{"endAngle": 3.141592653589793, "people": 6703, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 6488, "startAngle": 3.141592653589793}]},
                    {"color": "blue", "y_axis": 698, "x_axis": 2106, "station": "Airport", "traffic": [{"endAngle": 3.141592653589793, "people": 4876, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 2408, "startAngle": 3.141592653589793}]},
                    {"color": "blue", "y_axis": 642, "x_axis": 2163, "station": "Wood Island", "traffic": [{"endAngle": 3.141592653589793, "people": 1123, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 1066, "startAngle": 3.141592653589793}]},
                    {"color": "blue", "y_axis": 572, "x_axis": 2234, "station": "Orient Heights", "traffic": [{"endAngle": 3.141592653589793, "people": 2198, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 1398, "startAngle": 3.141592653589793}]},
                    {"color": "blue", "y_axis": 501, "x_axis": 2304, "station": "Suffolk Downs", "traffic": [{"endAngle": 3.141592653589793, "people": 486, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 115, "startAngle": 3.141592653589793}]},
                    {"color": "blue", "y_axis": 432, "x_axis": 2373, "station": "Beachmont", "traffic": [{"endAngle": 3.141592653589793, "people": 1592, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 1497, "startAngle": 3.141592653589793}]},
                    {"color": "blue", "y_axis": 364, "x_axis": 2441, "station": "Revere Beach", "traffic": [{"endAngle": 3.141592653589793, "people": 1950, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 494, "startAngle": 3.141592653589793}]},
                    {"color": "blue", "y_axis": 280, "x_axis": 2525, "station": "Wonderland", "traffic": [{"endAngle": 3.141592653589793, "people": 3226, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 162, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 178, "x_axis": 1800, "station": "Oak Grove", "traffic": [{"endAngle": 3.141592653589793, "people": 2746, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 2249, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 466, "x_axis": 1800, "station": "Sullivan Square", "traffic": [{"endAngle": 3.141592653589793, "people": 5921, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 5380, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 536, "x_axis": 1800, "station": "Community College", "traffic": [{"endAngle": 3.141592653589793, "people": 2264, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 2337, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 710, "x_axis": 1800, "station": "North Station", "traffic": [{"endAngle": 3.141592653589793, "people": 7709, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 7547, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 842, "x_axis": 1800, "station": "Haymarket", "traffic": [{"endAngle": 3.141592653589793, "people": 9466, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 7668, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 991, "x_axis": 1800, "station": "State Street", "traffic": [{"endAngle": 3.141592653589793, "people": 20, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 10, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 1114, "x_axis": 1748, "station": "Downtown Crossing", "traffic": [{"endAngle": 3.141592653589793, "people": 20, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 10, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 1198, "x_axis": 1662, "station": "Chinatown", "traffic": [{"endAngle": 3.141592653589793, "people": 4134, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 3461, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 1346, "x_axis": 1516, "station": "Tufts Medical Center", "traffic": [{"endAngle": 3.141592653589793, "people": 2351, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 2800, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 1415, "x_axis": 1445, "station": "Back Bay", "traffic": [{"endAngle": 3.141592653589793, "people": 7304, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 5801, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 1478, "x_axis": 1383, "station": "Mass Ave", "traffic": [{"endAngle": 3.141592653589793, "people": 3902, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 2799, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 1545, "x_axis": 1315, "station": "Ruggles", "traffic": [{"endAngle": 3.141592653589793, "people": 5042, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 4762, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 1611, "x_axis": 1249, "station": "Roxbury Crossing", "traffic": [{"endAngle": 3.141592653589793, "people": 2556, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 2360, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 1695, "x_axis": 1166, "station": "Jackson Square", "traffic": [{"endAngle": 3.141592653589793, "people": 2932, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 1389, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 1779, "x_axis": 1082, "station": "Stony Brook", "traffic": [{"endAngle": 3.141592653589793, "people": 1873, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 2079, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 1863, "x_axis": 999, "station": "Green Street", "traffic": [{"endAngle": 3.141592653589793, "people": 2034, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 1781, "startAngle": 3.141592653589793}]},
                    {"color": "orange", "y_axis": 1948, "x_axis": 914, "station": "Forest Hills", "traffic": [{"endAngle": 3.141592653589793, "people": 7439, "startAngle": 0}, {"endAngle": 6.283185307179586, "people": 7102, "startAngle": 3.141592653589793}]}];



var jsonCircles = [
    {
        "station": "Alewife",
        "x_axis": 987,
        "y_axis": 352
    },
    {
        "station": "Davis",
        "x_axis": 1078,
        "y_axis": 448
    },
    {
        "station": "Porter",
        "x_axis": 1173,
        "y_axis": 538
    },
    {
        "station": "Harvard",
        "x_axis": 1265,
        "y_axis": 632
    },
    {
        "station": "Central",
        "x_axis": 1359,
        "y_axis": 727
    },
    {
        "station": "Kendall",
        "x_axis": 1450,
        "y_axis": 817
    },
    {
        "station": "Charles/MGH",
        "x_axis": 1565,
        "y_axis": 931
    },
    {
        "station": "Park",
        "x_axis": 1637,
        "y_axis": 1006
    },
    {
        "station": "Downtown Crossing",
        "x_axis": 1748,
        "y_axis": 1115
    },
    {
        "station": "South Station",
        "x_axis": 1828,
        "y_axis": 1197
    },
    {
        "station": "Broadway",
        "x_axis": 1929,
        "y_axis": 1394
    },
    {
        "station": "Andrew",
        "x_axis": 1930,
        "y_axis": 1513
    },
    {
        "station": "JFK/UMass",
        "x_axis": 1928,
        "y_axis": 1627
    }
    {
        "station": "Savin Hill",
        "x_axis": 1824,
        "y_axis": 1913
    },
    {
        "station": "Fields Corner",
        "x_axis": 1824,
        "y_axis": 1965
    },
    {
        "station": "Shawmut",
        "x_axis": 1824,
        "y_axis": 2015
    },
    {
        "station": "Ashmont",
        "x_axis": 1824,
        "y_axis": 2065
    },
    {
        "station": "North Quincy",
        "x_axis": 2103,
        "y_axis": 1966
    },
    {
        "station": "Wollaston",
        "x_axis": 2175,
        "y_axis": 2037
    },
    {
        "station": "Quincy Center",
        "x_axis": 2248,
        "y_axis": 2111
    },
    {
        "station": "Quincy Adams",
        "x_axis": 2300,
        "y_axis": 2187
    },
    {
        "station": "Braintree",
        "x_axis": 2300,
        "y_axis": 2297
    },
    {
        "station": "Bowdoin",
        "x_axis": 1643,
        "y_axis": 846
    },
    {
        "station": "State",
        "x_axis": 1800,
        "y_axis": 991
    },
    {
        "station": "Aquarium",
        "x_axis": 1901,
        "y_axis": 903
    },
    {
        "station": "Maverick",
        "x_axis": 2053,
        "y_axis": 754
    },
    {
        "station": "Airport",
        "x_axis": 2106,
        "y_axis": 698
    },
    {
        "station": "Wood Island",
        "x_axis": 2163,
        "y_axis": 642
    },
    {
        "station": "Orient Heights",
        "x_axis": 2234,
        "y_axis": 572
    },
    {
        "station": "Suffolk Downs",
        "x_axis": 2304,
        "y_axis": 501
    },
    {
        "station": "Beachmont",
        "x_axis": 2373,
        "y_axis": 432
    },
    {
        "station": "Revere Beach",
        "x_axis": 2441,
        "y_axis": 364
    },
    {
        "station": "Wonderland",
        "x_axis": 2525,
        "y_axis": 280
    },
    {
        "station": "Oak Grove",
        "x_axis": 1800,
        "y_axis":178
    },
    {
        "station": "Malden Center",
        "x_axis": 1800,
        "y_axis": 250
    },
    {
        "station": "Wellington",
        "x_axis": 1800,
        "y_axis": 323
    },
    {
        "station": "Assembly",
        "x_axis": 1800,
        "y_axis": 393
    },
    {
        "station": "Sullivan Square",
        "x_axis": 1800,
        "y_axis": 466
    },
    {
        "station": "Community College",
        "x_axis": 1800,
        "y_axis": 536
    },
    {
        "station": "North Station",
        "x_axis": 1800,
        "y_axis": 710
    },
    {
        "station": "Haymarket",
        "x_axis": 1800,
        "y_axis": 842
    },
    {
        "station": "State",
        "x_axis": 1800,
        "y_axis": 991
    },
    {
        "station": "Downtown Crossing",
        "x_axis": 1748,
        "y_axis": 1114
    },
    {
        "station": "Chinatown",
        "x_axis": 1662,
        "y_axis": 1198
    },
    {
        "station": "Tufts",
        "x_axis": 1516,
        "y_axis": 1346
    },
    {
        "station": "Back Bay",
        "x_axis": 1445,
        "y_axis": 1415
    },
    {
        "station": "Mass Ave",
        "x_axis": 1383,
        "y_axis": 1478
    },
    {
        "station": "Ruggles",
        "x_axis": 1315,
        "y_axis": 1545
    },
    {
        "station": "Roxbury Crossing",
        "x_axis": 1249,
        "y_axis": 1611
    },
    {
        "station": "Jackson Sq",
        "x_axis": 1166,
        "y_axis": 1695
    },
    {
        "station": "Stony Brook",
        "x_axis": 1082,
        "y_axis": 1779
    },
    {
        "station": "Green St",
        "x_axis": 999,
        "y_axis": 1863
    },
    {
        "station": "Forest Hills",
        "x_axis": 914,
        "y_axis": 1948
    }
];


var svgContainer = d3.select("body").append("svg")
                                    .attr("width", 3000)
                                    .attr("height", 3000);

var circles - svgContainer.selectAll("circle")
                            .data(jsonCircles)
                            .enter()
                            .append("circle");

var circleAttributes = circles
                        .attr("cx", function (d) {return d.x_axis})
                        .attr("cy", function (d) {return d.y_axis});
