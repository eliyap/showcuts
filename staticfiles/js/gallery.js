$(document).ready(function () {
    $(".sc-card").each(function (){
        $(this).children(".action").last().addClass('cutoff');
    })
});