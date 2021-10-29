

$(function () {
    var eval = document.getElementById('eval');
    eval.disabled = true; 
    var path;
    $(".dropdown-item")[0].checked = false;
    $(".dropdown-item")[1].checked = false;
    $(".dropdown-item")[2].checked = false;
    $(".dropdown-item")[3].checked = false;
    $(".dropdown-item")[4].checked = false;
    $(".dropdown-item")[5].checked = false;
    $(".dropdown-item")[6].checked = false;
    $(".dropdown-item")[7].checked = false;

    $("#load_button").click(function (){
        $('#imgupload').trigger('click');
    });
    
    $("#imgupload").change(function (event){
        var image = document.getElementById('imgRX');
        image.src = URL.createObjectURL( event.target.files[0]);
        path = event.target.files[0].name;
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
            alert(
                "Covid "+ data['Covid'].toFixed(2)+" %\n"+
                "Normal "+ data['Normal'].toFixed(2)+" %\n"+
                "Viral "+ data['Viral'].toFixed(2)+"%\n")
        });
    });

    $(".dropdown-item").click(function (){
        eval.disabled = false;
        if(this.style.backgroundColor == ""){
            this.style.backgroundColor = "#83c45d";
            this.checked = true; 
        }else{
            this.style.backgroundColor = "";
            this.checked = false;
        }
        
    });
});