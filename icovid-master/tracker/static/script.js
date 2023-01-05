$(document).ready(function(){
    $("#prov_container").hide();
    let new_chart = null;
    let new_chart2 = null;
    let active_chart = 'positif';

    $.getJSON("https://apicovid19indonesia-v2.vercel.app/api/indonesia", 
    function(data){
        $('#jumlah_positif').text(data.positif.toLocaleString("en-US"));
        $('#jumlah_sembuh').text(data.sembuh.toLocaleString("en-US"));
        $('#jumlah_meninggal').text(data.meninggal.toLocaleString("en-US"));
    });

    $.getJSON("https://apicovid19indonesia-v2.vercel.app/api/indonesia/harian", 
    function(data){
        const dataset_positif = [];
        const dataset_sembuh = [];
        const dataset_meninggal = [];
        const dataset_positif2 = [];
        const dataset_sembuh2 = [];
        const dataset_meninggal2 = [];
        const dateset = [];
        for (let i = data.length-dataCount; i < data.length; i++){
            dataset_positif.push(data[i].positif_kumulatif);
            dataset_sembuh.push(data[i].sembuh_kumulatif);
            dataset_meninggal.push(data[i].meninggal_kumulatif);
            dataset_positif2.push(data[i].positif);
            dataset_sembuh2.push(data[i].sembuh);
            dataset_meninggal2.push(data[i].meninggal);
            dateset.push(data[i].tanggal.split('T')[0]);
        }

        let indo_chart = document.getElementById('indo_chart');
        let indo_chart2 = document.getElementById('indo_chart2');
        if (indo_chart != null){
            indo_chart = indo_chart.getContext('2d');
        }
        if (indo_chart2 != null){
            indo_chart2 = indo_chart2.getContext('2d');
        }

        if (indo_chart != null){
            new_chart = new Chart(indo_chart, {
                type: 'line',
                data: {
                    labels: dateset,
                    datasets: [{
                        label: 'Positif',
                        data: dataset_positif,
                        backgroundColor: 'rgb(255, 188, 188)',
                        borderColor: 'rgb(255, 188, 188)'
                    },{
                        label: 'Sembuh',
                        data: dataset_sembuh,
                        backgroundColor: 'rgb(40, 255, 191)',
                        borderColor: 'rgb(40, 255, 191)',
                        hidden: true
                    },{
                        label: 'Meninggal',
                        data: dataset_meninggal,
                        backgroundColor: 'rgb(243, 139, 160)',
                        borderColor: 'rgb(243, 139, 160)',
                        hidden: true
                    }]
                },
                options: {
                    plugins: {
                        legend: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: "Grafik Kumulatif Harian"
                        }
                    }
                }
            })
        }
        if (indo_chart2 != null){
            new_chart2 = new Chart(indo_chart2, {
                type: 'line',
                data: {
                    labels: dateset,
                    datasets: [{
                        label: 'Positif',
                        data: dataset_positif2,
                        backgroundColor: 'rgb(255, 188, 188)',
                        borderColor: 'rgb(255, 188, 188)'
                    },{
                        label: 'Sembuh',
                        data: dataset_sembuh2,
                        backgroundColor: 'rgb(40, 255, 191)',
                        borderColor: 'rgb(40, 255, 191)',
                        hidden: true
                    },{
                        label: 'Meninggal',
                        data: dataset_meninggal2,
                        backgroundColor: 'rgb(243, 139, 160)',
                        borderColor: 'rgb(243, 139, 160)',
                        hidden: true
                    }]
                },
                options: {
                    plugins: {
                        legend: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: "Grafik Harian"
                        }
                    }
                }
            })
        }
        
    });

    $("#btnradio1").click(function(){
        if (active_chart != 'positif'){
            active_chart = 'positif';
            if (new_chart != null){
                new_chart.data.datasets[0].hidden = false;
                new_chart.data.datasets[1].hidden = true;
                new_chart.data.datasets[2].hidden = true;
                new_chart.update();
            }
            if (new_chart2 != null){
                new_chart2.data.datasets[0].hidden = false;
                new_chart2.data.datasets[1].hidden = true;
                new_chart2.data.datasets[2].hidden = true;
                new_chart2.update();
            }  
        }
    })

    $("#btnradio2").click(function(){
        if (active_chart != 'sembuh'){
            active_chart = 'sembuh';
            if (new_chart != null){
                new_chart.data.datasets[0].hidden = true;
                new_chart.data.datasets[1].hidden = false;
                new_chart.data.datasets[2].hidden = true;
                new_chart.update();
            }
            if (new_chart2 != null){
                new_chart2.data.datasets[0].hidden = true;
                new_chart2.data.datasets[1].hidden = false;
                new_chart2.data.datasets[2].hidden = true;
                new_chart2.update();
            } 
        }
    })

    $("#btnradio3").click(function(){
        if (active_chart != 'meninggal'){
            active_chart = 'meninggal';
            if (new_chart != null){
                new_chart.data.datasets[0].hidden = true;
                new_chart.data.datasets[1].hidden = true;
                new_chart.data.datasets[2].hidden = false;
                new_chart.update();
            }
            if (new_chart2 != null){
                new_chart2.data.datasets[0].hidden = true;
                new_chart2.data.datasets[1].hidden = true;
                new_chart2.data.datasets[2].hidden = false;
                new_chart2.update();
            } 
        }
    })

    $("#button_prov").click(function(){
        const inp = $("#input_prov").val();
        $.getJSON("https://apicovid19indonesia-v2.vercel.app/api/indonesia/provinsi", 
        function(data){
            let found = false;
            for (let i in data){
                if (data[i].provinsi.toLowerCase() === inp.toLowerCase()){
                    $('#prov-name').text(data[i].provinsi);
                    $('#jumlah_positif_prov').text(data[i].kasus.toLocaleString("en-US"));
                    $('#jumlah_sembuh_prov').text(data[i].sembuh.toLocaleString("en-US"));
                    $('#jumlah_meninggal_prov').text(data[i].meninggal.toLocaleString("en-US"));
                    found = true;
                    break;
                }
            }
            if (found){
                $("#prov_container").show();
            }
        });
    });
});