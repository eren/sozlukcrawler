/**
 * Created by eren on 19/12/14.
 */

 $(function () {

    $('#rte_toplam_girdi').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: 1,//null,
            plotShadow: false
        },
        title: {
            text: 'Tüm Zamanda Toplam Girdi Sayısı'
        },
        subtitle: {
            text: 'Recep Tayyip Erdoğan (Toplam: 170.602)'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.y}</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: % {point.percentage:.1f}',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            type: 'pie',
            name: 'Girdi Sayısı',
            data: [
                ['Ekşisözlük',   44592],
                ['Uludağsözlük',       22785],
                ['İtüsözlük',   13308]
            ]
        }]
    });



    $('#rte_yil').highcharts({
        chart: {
            type: 'spline'
        },
        title: {
            text: 'Yıllara Göre Girdi Dağılımı'
        },
        subtitle: {
            text: 'Recep Tayyip Erdoğan'
        },
        xAxis: {
            type: 'datetime',
            labels: {
                format: '{value:%Y}',
                rotation: 90,
                align: 'left'
            },
            title: {
                text: 'Yıl'
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
            pointFormat: '{point.x:%Y}: {point.y} girdi'
        },

        series: [{
            name: 'Ekşisözlük',
            // Define the data points. All series have a dummy year
            // of 1970/71 in order to be compared on the same x axis. Note
            // that in JavaScript, months start at 0 for January, 1 for February etc.
            data: [
[Date.UTC(2001, 1), 7],
[Date.UTC(2002, 1), 28],
[Date.UTC(2003, 1), 47],
[Date.UTC(2004, 1), 154],
[Date.UTC(2005, 1), 370],
[Date.UTC(2006, 1), 769],
[Date.UTC(2007, 1), 708],
[Date.UTC(2008, 1), 781],
[Date.UTC(2009, 1), 1529],
[Date.UTC(2010, 1), 2688],
[Date.UTC(2011, 1), 5546],
[Date.UTC(2012, 1), 5832],
[Date.UTC(2013, 1), 13793],
[Date.UTC(2014, 1), 12340]
            ]
        }, {
            name: 'Uludağsözlük',
            data: [
[Date.UTC(2006, 1), 264],
[Date.UTC(2007, 1), 807],
[Date.UTC(2008, 1), 862],
[Date.UTC(2009, 1), 1342],
[Date.UTC(2010, 1), 2225],
[Date.UTC(2011, 1), 3634],
[Date.UTC(2012, 1), 2662],
[Date.UTC(2013, 1), 5576],
[Date.UTC(2014, 1), 5412]
            ]
        }, {
            name: 'İtüsözlük',
            data: [
[Date.UTC(2004, 1), 22],
[Date.UTC(2005, 1), 37],
[Date.UTC(2006, 1), 75],
[Date.UTC(2007, 1), 449],
[Date.UTC(2008, 1), 272],
[Date.UTC(2009, 1), 645],
[Date.UTC(2010, 1), 1075],
[Date.UTC(2011, 1), 1553],
[Date.UTC(2012, 1), 1533],
[Date.UTC(2013, 1), 4093],
[Date.UTC(2014, 1), 3554]
            ]
        }]
    });
});