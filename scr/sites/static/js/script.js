

$(function () {
    $("#eval")[0].disabled = true; 
    $("#dropdown")[0].disabled = true; 

    $(".dropdown-item")[0].checked = false;
    $(".dropdown-item")[1].checked = false;
    $(".dropdown-item")[2].checked = false;
    $(".dropdown-item")[3].checked = false;
    $(".dropdown-item")[4].checked = false;
    $(".dropdown-item")[5].checked = false;
    $(".dropdown-item")[6].checked = false;
    $(".dropdown-item")[7].checked = false;


    const ctx = $('#myChart');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Covid', 'Normal', 'Viral'],
            datasets: [{
                label:'Diagnostico',

                data: [91, 1, 9],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.52)',
                    'rgba(54, 162, 235, 0.52)',
                    'rgba(255, 206, 86, 0.52)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            legend: {
                display: false
            }
        }
    });
    

    $("#load_button").click(function (){
        $('#imgupload').trigger('click');
    });
    
    $("#imgupload").change(function (event){
        var image = document.getElementById('imgRX');
        image.src = URL.createObjectURL( event.target.files[0]);
        path = event.target.files[0].name;
        $("#dropdown")[0].disabled = false; 
    });
    
    $("#eval").click(function (){
        json_object = {
            "vgg":$("#vgg")[0].checked,
            "dense":$("#dense")[0].checked,
            "mobil":$("#mobil")[0].checked,
            "alex":$("#alex")[0].checked,
            "efficient":$("#efficient")[0].checked,
            "inception":$("#inception")[0].checked,
            "resnet":$("#resnet")[0].checked,
            "rexnet":$("#rexnet")[0].checked,
            "img_file":path
        };
        $.post('/evaluate',json_object).done(function(data){
                $("#imgHeatMap")[0].src = "static/images/heatmap.png";
                $(".piechart").css("visibility","visible");
                myChart.data.datasets[0].data[0] = data['Covid'];
                myChart.data.datasets[0].data[1] = data['Normal'];
                myChart.data.datasets[0].data[2] = data['Viral'];
                
                var max = 'Covid';
                if(data['Normal']>max){max='Normal';}
                if(data['Viral']>max){max='Viral';}
                myChart.data.datasets[0].label = "Diagnostico: " + max;
                myChart.update();
                ctx.css("visibility","visible");

            });
        });
        
        $(".dropdown-item").click(function (){
            $("#eval")[0].disabled = false; 
            if(this.style.backgroundColor == ""){
                this.style.backgroundColor = "#83c45d";
                this.checked = true; 
            }else{
                this.style.backgroundColor = "";
                this.checked = false;
            }
        
    });
});