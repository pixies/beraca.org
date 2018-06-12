var url_ = "http://projetos.institutoberaca.org/"
//var url_ = "http://localhost:8000/"
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
            $.getJSON(url_ + "api/client/get_categories/2"+ this.options[this.selectedIndex].value, function (data) {
                $.each(data, function (key, value) {
                    // APPEND OR INSERT DATA TO SELECT ELEMENT.
                    $('#categories').append('<option value="' + value + '">' + key + '</option>');
                });
            });


        });
     });

$('button').click(function () {
        var val = $(this).val();
        //alert($('#categories').val());
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
