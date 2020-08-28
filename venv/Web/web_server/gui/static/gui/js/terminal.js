$(document).ready(function () {
    var len = 0;
    var state = 0;
    console.log(len);
    $(".mkfile").css('display', 'none');
    $("#text").css({'height' : '300px','width':'500px'});
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
                len = response.len;
                state = $("#terminal").val().length;
 
            }
        });
    });
    
    $("#check").click(function (e) {
        var txt = $("#terminal").val();
        var resta = txt.length - state
        var command = txt.substr(txt.length - (resta + len));
        console.log(command);
        $.ajax({
            type: "POST",
            url: "check_command",
            data: {
                'command' : command,
            },
            dataType: "json",
            success: function (response) {
                if (response.data == '2'){
                    $(".mkfile").css('display', 'Block');
                }
                else{
                    $("#terminal").val($("#terminal").val() + "\n" + response.data);
                    len = response.len;
                    state = $("#terminal").val().length;
 
                }

            }
        });
    });
    $("#check2").click(function (e) {
        var txt = $("#terminal").val();
        var resta = txt.length - state
        var command = txt.substr(txt.length - (resta + len));
        console.log(command);
        $.ajax({
            type: "POST",
            url: "check_command",
            data: {
                'command' : 2,
                'command2' : command,
                'data' : $("#text").val(),
            },
            dataType: "json",
            success: function (response) {
                if (response.data == '2'){
                    $(".mkfile").css('display', 'Block');
                }
                else{
                    $("#terminal").val($("#terminal").val() + "\n" + response.data);
                    len = response.len;
                    state = $("#terminal").val().length;
                    $(".mkfile").css('display', 'none');
 
                }

            }
        });
    });   
});