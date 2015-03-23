//23 Mart 2015
//-- Eren

$(function () {
    $('#trden_gitmek_ay').highcharts({
        chart: {
            type: 'spline'
        },
        title: {
            text: 'Aylara Göre Girdi Dağılımı'
        },
        subtitle: {
            text: "Toplam girdi: <b>3064</b>"
        },
        xAxis: {
            type: 'datetime',
            dateTimeLabelFormats: { // don't display the dummy year
                month: '%e. %b',
                year: '%b'
            },
            labels: {
                format: '{value:%Y-%m}',
                rotation: 45,
                align: 'left'
            },

            title: {
                text: 'Tarih'
            }
        },
        yAxis: {
            title: {
                text: 'Girdi sayısı'
            },
            min: 0
        },
        tooltip: {
            headerFormat: '<b>{series.name}</b><br>',
            pointFormat: '{point.x:%Y-%m}: {point.y} girdi'
        },

        series: [{
            name: 'Ekşisözlük',
            // Define the data points. All series have a dummy year
            // of 1970/71 in order to be compared on the same x axis. Note
            // that in JavaScript, months start at 0 for January, 1 for February etc.
            data: [
                [Date.UTC(2012, 7), 3],
                [Date.UTC(2012, 8), 0],
                [Date.UTC(2012, 9), 0],
                [Date.UTC(2012, 10), 0],
                [Date.UTC(2012, 11), 0],
                [Date.UTC(2013, 0), 0],
                [Date.UTC(2013, 1), 0],
                [Date.UTC(2013, 2), 0],
                [Date.UTC(2013, 3), 0],
                [Date.UTC(2013, 4), 397],
                [Date.UTC(2013, 5), 268],
                [Date.UTC(2013, 6), 25],
                [Date.UTC(2013, 7), 133],
                [Date.UTC(2013, 8), 76],
                [Date.UTC(2013, 9), 5],
                [Date.UTC(2013, 10), 11],
                [Date.UTC(2013, 11), 165],
                [Date.UTC(2014, 0), 136],
                [Date.UTC(2014, 1), 156],
                [Date.UTC(2014, 2), 481],
                [Date.UTC(2014, 3), 117],
                [Date.UTC(2014, 4), 53],
                [Date.UTC(2014, 5), 42],
                [Date.UTC(2014, 6), 61],
                [Date.UTC(2014, 7), 184],
                [Date.UTC(2014, 8), 37],
                [Date.UTC(2014, 9), 211],
                [Date.UTC(2014, 10), 132],
                [Date.UTC(2014, 11), 88],
                [Date.UTC(2015, 0), 55],
                [Date.UTC(2015, 1), 188],
                [Date.UTC(2015, 2), 40]
                ]
        }]
    });
});
