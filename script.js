


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
