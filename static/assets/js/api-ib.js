//var url_ = "http://projetos.institutoberaca.org/"
//var url_ = "http://localhost:8000/"
var url_ = "http://45.55.202.61:8080/"
$(document).ready(function () {
        // EXTRACT JSON DATA.
        $.getJSON(url_ + "api/client/get_products/", function (data) {

            $.each(data, function (index, value) {
                // APPEND OR INSERT DATA TO SELECT ELEMENT.
                $('#products').append('<option value="' + value.id + '">' + value.common_name + '</option>');

            });
        });
        //valor = $('#msg').text(this.options[this.selectedIndex].value);
        // SELECT change EVENT TO READ SELECTED VALUE FROM DROPDOWN LIST.

});

$(document).ready(function () {

        $('#products').change(function () {
            // EXTRACT JSON DATA.
            $.getJSON(url_ + "api/client/get_projects/" + this.options[this.selectedIndex].value, function (data) {
                $('#range').empty();
                $('#range').append('<option value="">Investment range</option>');
                $.each(data, function (key, value) {
                    // APPEND OR INSERT DATA TO SELECT ELEMENT.
                    $('#range').append('<option value="' + value + '">' + key + '</option>');
                });
            });

            //$('range').text('Selected Item: ' + this.options[this.selectedIndex].value);
            //$('#msg1').text(this.options[this.selectedIndex].value);
        });
     });

$(document).ready(function () {

        $('#range').change(function () {
            // EXTRACT JSON DATA.
            
                    $('#categories').empty();
                    $('#categories').append('<option value="">Type of projects</option>');
            id_cat_vet = this.options[this.selectedIndex].value.split(",");
            //alert(id_cat_vet.length);
            if(id_cat_vet.length>0){
                var i;
                var lista='';
                //alert(id_cat_vet.length);
                for(i=0;i<id_cat_vet.length;i++){
                    if(i==0){
                        lista+=''+id_cat_vet[i];
                    }else{
                        lista+=','+id_cat_vet[i];
                    }
                    //alert('for');
                }
                    $.getJSON(url_ + "api/client/get_categories/"+lista, function (data) {
                        //alert('link');
                        $.each(data, function (key, value) {
                            //alert('populando option');
                            // APPEND OR INSERT DATA TO SELECT ELEMENT.
                            $('#categories').append('<option value="' + value + '">' + key + '</option>');
                        });
                    });
                
            }else{
                $.getJSON(url_ + "api/client/get_categories/"+ this.options[this.selectedIndex].value, function (data) {
                    //alert('fora do cat');
                    $.each(data, function (key, value) {
                        // APPEND OR INSERT DATA TO SELECT ELEMENT.
                        $('#categories').append('<option value="' + value + '">' + key + '</option>');






                    });

                });
            }


        });
     });

$('#button-search').click(function () {
        $('#resultado').empty();
        var id_cat_vet = $('#categories').val().split(",");
        var i;

        if($('#range option:selected').text()=='Investment range' || $('#products option:selected').text()=='Product' || $('#categories option:selected').text()=='Type of project'){
            $('#resposta').append("</div><div class='col-12 center alert alert-danger'>é necessário preencher os campos.</div>");

            setTimeout(function(){ $('#resposta').empty(); }, 2000);

        }else{
        
            if(id_cat_vet.length>0){
                for(i=0;i<id_cat_vet.length;i++){
                    $.ajax({
                        url: url_ + "api/project/detail/" + id_cat_vet[i],
                        method: "GET",
                        headers: {"Accept": "application/json; odata=verbose"},
                        success: function (data) {
                      //      alert(data);
                            //$('body').html(JSON.stringify(data));
                            //console.log(JSON.stringify(data));
                                var url_path = "/index/projeto/" + data.id;
                                //$('#resultado').append("<i class='nc-icon nc-minimal-right text-white'></i><a class='product_name' href='" + url_path + "'>" + data.name + "</a><p>R$ " + data.project_totals + "</p>");
                                document.getElementById("msgresult").innerHTML="<h6>Exibindo resultados de projetos com range de investimento "+$('#range option:selected').text()+". Clique no título do projeto para saber mais</h6>";
                                $('#resultado').append("<div class='col-12'><a class='product_name btn btn-link btn-danger' href='" + url_path + "'><i class='nc-icon nc-minimal-right'></i>" + data.name + "</a></div><div class='col-12 text-left'><p class='desciption_text ml-5'>US " + data.project_totals + "</p></div>");


                        },
                        error: function (data) {
                            $('body').html(data);
                            //console.log("error");
                        }
                    });
                }
                }else{
                        $.ajax({
                        url: url_ + "api/project/detail/" + $('#categories').val(),
                        method: "GET",
                        headers: {"Accept": "application/json; odata=verbose"},
                        success: function (data) {
                      //      alert(data);
                            //$('body').html(JSON.stringify(data));
                            //console.log(JSON.stringify(data));
                                var url_path = "/index/projeto/" + data.id
                                //$('#resultado').append("<i class='nc-icon nc-minimal-right text-white'></i><a class='product_name' href='" + url_path + "'>" + data.name + "</a><p>R$ " + data.project_totals + "</p>");
                                $('#resultado').append("<a class='product_name btn btn-link btn-danger' href='" + url_path + "'><i class='nc-icon nc-minimal-right'></i>" + data.name + "</a><p class='desciption_text pull-right mt-3'>US " + data.project_totals + "</p>");



                        },
                        error: function (data) {
                            $('body').html(data);
                            //console.log("error");
                        }
                    });
            }
        }
    });

/**
        $("#products").change(function () {
            $.getJSON('http://localhost:8000/api/client/getprojects/1', function(result2){
                $.each(result2, function(key, value){
                    projectsOptions+="<option value='" + value.id + "'>" + value. + "</option>";
            });
            $('#range').html(projectsOptions);

        });

        });
}); **/


function myFunction() {

    var postData = [];

    $.ajax({
    url: url_ + 'api/project/support/create/',
    type: "POST",
    data: {"event":{ "project": 5,"client": 2 }},
    dataType:'json',
    success: function (response) {
        console.log(response);
    },
    error: function(error){
        console.log("Something went wrong", error);
    }
});


};
