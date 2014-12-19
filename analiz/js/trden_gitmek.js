/**
 * Created by eren on 19/12/14.
 */
     //
     // Türkiye'den Siktir Olup Gitmek
     //
$(function () {
    $('#trden_gitmek_yil').highcharts({
        chart: {
            type: 'spline'
        },
        title: {
            text: 'Yıllara Göre Girdi Dağılımı'
        },
        subtitle: {
            text: "Türkiye'den Siktir Olup Gitmek (Toplam girdi: <b>3304</b>)"
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
[Date.UTC(2012, 1), 3],
[Date.UTC(2013, 1), 1097],
[Date.UTC(2014, 1), 1728]
            ]
        }, {
            name: 'Uludağsözlük',
            data: [
[Date.UTC(2013, 1), 37],
[Date.UTC(2014, 1), 80]
            ]
        }, {
            name: 'İtüsözlük',
            data: [
[Date.UTC(2013, 1), 103],
[Date.UTC(2014, 1), 256]
            ]
        }]
    });

    $('#trden_gitmek_toplam_girdi').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: 1,//null,
            plotShadow: false
        },
        title: {
            text: 'Tüm Zamanda Toplam Girdi Sayısı'
        },
        subtitle: {
            text: "Türkiye'den Siktir Olup Gitmek (Toplam girdi: <b>3304</b>)"
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
                ['Ekşisözlük',   2828],
                ['Uludağsözlük', 117],
                ['İtüsözlük',    359]
            ]
        }]
    });
});