$(document).ready(function() {
  console.log("ready!");

  $('form').on('submit', function() {

    //console.log("the form has beeen submitted");
    console.log("start");
    //var imageurlone = $('#imageurl').val();
    var imageurlone = $('input[name="imageurl"]').val()

      //var imageurlone = 'http://www.homedepot.com/catalog/productImages/1000/a6/a619a055-6979-4b47-b0da-5dfa09d6ca2b_1000.jpg';


    console.log(imageurlone);
    console.log("end");


    $.ajax({
            type: "POST",
            url: "/",
            data : { 'imageurl': imageurlone},
            beforeSend: function(){
            $('#image').show();
            },
            complete: function(){
                $('#image').hide();
            },
            success: function(results) {
            console.log(results);
            var output = document.getElementById('output');
            output.innerHTML = results;
              //$("#results").html(results.faucet)
              //$("input").val("")
            },
            error: function(error) {
              //console.log(error);
            }

        });


  });

});
