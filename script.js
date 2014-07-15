d3.csv("/Users/ashleycuster/Desktop/StationCountsByMinute_2014_02-01--03-02.csv", function(d) {
    return {
        station: d.station,
        datetime: new Date(d.datetime.replace(/\s+/g, 'T')),
        entries: parseInt(d.entries),
        exits: parseInt(d.exits)
    };
},  function(error, rows) {
        console.log(rows);
    }
);
