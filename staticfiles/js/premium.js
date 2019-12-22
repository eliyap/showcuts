$(document).ready(function () {
    $("#get-premium").click(
        function (){
            $.ajax({
            type: "GET",
            url: window.location.origin + "/share/premium",
            data: {},
            success: function () {
                location.reload(); 
            }
        });
    })
})
