$(document).ready(function () {
    $("#check").click(function (e) { 
        $.ajax({
            type: "GET",
            url: "check_user",
            data: {
                'user' : $("#user").val(),
                'password' : $("#password").val(),
            },
            dataType: "json",
            success: function (response) {
                if (response.check == 1) {
                    $(location).attr('href', '/terminal');
                }
                else{
                    alert("Usuario o contraseña incorrecta");
                }
            }
        });        
    });
});