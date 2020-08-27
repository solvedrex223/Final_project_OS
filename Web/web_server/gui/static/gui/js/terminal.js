$(document).ready(function () {
    var len = 0;
    console.log(len);
    $("#terminal").ready(function () {
        $.ajax({
            type: "POST",
            url: "check_command",
            data: {
                'command' : 1,
            },  
            dataType: "json",
            success: function (response) {
                $("#terminal").val(response.data);
                // len = $("#terminal").val().length;
                // console.log(len);
            }
        });
    });
    
    $("#check").click(function (e) {
        console.log(len);
        var txt = $("#terminal").val();
        var command = txt.substr(len - 10);
        console.log(command);
        $.ajax({
            type: "POST",
            url: "check_command",
            data: {
                'command' : command,
            },
            dataType: "json",
            success: function (response) {
                $("#terminal").val($("#terminal").val() + "\n" + response.data);
                len = $("#terminal").val().length;
            }
        });
    });
    
});