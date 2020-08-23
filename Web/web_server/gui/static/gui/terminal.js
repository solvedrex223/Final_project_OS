$(document).ready(function () {
    $("#check").click(function (e) {
        var command = $("#terminal").val();
        console.log(command);
        $.ajax({
            type: "POST",
            url: "check_command",
            data: {
                'command' : command,
            },
            dataType: "json",
            success: function (response) {
                console.log(response.command);
                console.log(response.dir);
                
            }
        });
    });
    
});