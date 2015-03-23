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
                [Date.UTC(2012, 8), 3],
                [Date.UTC(2012, 9), 0],
                [Date.UTC(2012, 10), 0],
                [Date.UTC(2012, 11), 0],
                [Date.UTC(2012, 12), 0],
                [Date.UTC(2013, 1), 0],
                [Date.UTC(2013, 2), 0],
                [Date.UTC(2013, 3), 0],
                [Date.UTC(2013, 4), 0],
                [Date.UTC(2013, 5), 397],
                [Date.UTC(2013, 6), 268],
                [Date.UTC(2013, 7), 25],
                [Date.UTC(2013, 8), 133],
                [Date.UTC(2013, 9), 76],
                [Date.UTC(2013, 10), 5],
                [Date.UTC(2013, 11), 11],
                [Date.UTC(2013, 12), 165],
                [Date.UTC(2014, 1), 136],
                [Date.UTC(2014, 2), 156],
                [Date.UTC(2014, 3), 481],
                [Date.UTC(2014, 4), 117],
                [Date.UTC(2014, 5), 53],
                [Date.UTC(2014, 6), 42],
                [Date.UTC(2014, 7), 61],
                [Date.UTC(2014, 8), 184],
                [Date.UTC(2014, 9), 37],
                [Date.UTC(2014, 10), 211],
                [Date.UTC(2014, 11), 132],
                [Date.UTC(2014, 12), 88],
                [Date.UTC(2015, 1), 55],
                [Date.UTC(2015, 2), 188],
                [Date.UTC(2015, 3), 40]
                ]
        }]
    });
});