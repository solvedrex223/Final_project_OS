$(document).ready(function () {
    $("#check").click(function (e) { 
       $.ajax({
           type: "POST",
           url: "check_user",
           data: {
               'user': $("#user").val(),
               'password' : $("#password").val(),
           },
           dataType: "json",
           success: function (response) {
               console.log(response.check);
               if (response.check == 1) {
                   $(location).attr('href', '/');
               }
               else{
                   alert ("El usuario ya existe");
               }
           }
       });
        
    });
});