/**
 * Created by eren on 19/12/14.
 */

     //
     // Partiler
     ///
 $(function () {
    $('#eksisozluk_partiler').highcharts({
        chart: {
            type: 'spline'
        },
        title: {
            text: 'Yıllara Göre Girdi Dağılımı'
        },
        subtitle: {
            text: "Kaynak: ekşisözlük (Toplam girdi: <b>13.759</b>)"
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
            name: 'AKP',
            data: [
[Date.UTC(2001, 1), 6],
[Date.UTC(2002, 1), 33],
[Date.UTC(2003, 1), 13],
[Date.UTC(2004, 1), 32],
[Date.UTC(2005, 1), 58],
[Date.UTC(2006, 1), 107],
[Date.UTC(2007, 1), 326],
[Date.UTC(2008, 1), 264],
[Date.UTC(2009, 1), 250],
[Date.UTC(2010, 1), 344],
[Date.UTC(2011, 1), 1028],
[Date.UTC(2012, 1), 939],
[Date.UTC(2013, 1), 1324],
[Date.UTC(2014, 1), 1328]
            ]
        }, {
            name: 'CHP',
            data: [
[Date.UTC(2000, 1), 2],
[Date.UTC(2001, 1), 2],
[Date.UTC(2002, 1), 15],
[Date.UTC(2003, 1), 7],
[Date.UTC(2004, 1), 28],
[Date.UTC(2005, 1), 26],
[Date.UTC(2006, 1), 42],
[Date.UTC(2007, 1), 286],
[Date.UTC(2008, 1), 118],
[Date.UTC(2009, 1), 207],
[Date.UTC(2010, 1), 513],
[Date.UTC(2011, 1), 1067],
[Date.UTC(2012, 1), 422],
[Date.UTC(2013, 1), 1002],
[Date.UTC(2014, 1), 1847]
            ]
        }, {
            name: 'MHP',
            data: [
[Date.UTC(2000, 1), 1],
[Date.UTC(2001, 1), 1],
[Date.UTC(2002, 1), 9],
[Date.UTC(2003, 1), 1],
[Date.UTC(2004, 1), 8],
[Date.UTC(2005, 1), 9],
[Date.UTC(2006, 1), 4],
[Date.UTC(2007, 1), 71],
[Date.UTC(2008, 1), 113],
[Date.UTC(2009, 1), 67],
[Date.UTC(2010, 1), 113],
[Date.UTC(2011, 1), 404],
[Date.UTC(2012, 1), 360],
[Date.UTC(2013, 1), 327],
[Date.UTC(2014, 1), 635]
            ]
        }]
    });


    $('#eksisozluk_partiler_toplam').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: 1,//null,
            plotShadow: false
        },
        title: {
            text: 'Partilerin Toplam Girdisi'
        },
        subtitle: {
            text: "Kaynak: ekşisözlük (Toplam girdi: <b>13.759</b>)"
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
                ['AKP',   6052],
                ['CHP', 5584],
                ['MHP',    2123]
            ]
        }]
    });

// end
});