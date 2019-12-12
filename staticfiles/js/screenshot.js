

$(document).ready(function () {
    $("#screenshot").click(function () {
        $("#action-container").prepend($(".sc-title").clone().css({
            'position': 'absolute',
            'top': '1.5rem',
            'left': '2rem',
        }));
        $("#screenshot-mark").css({'display':'block'});
        
        domtoimage.toBlob(document.getElementById('action-container'))
            .then(function (blob) {
                window.saveAs(blob, $(document).attr('title')+'.png');
            }).then(function(){
                $("#action-container>.sc-title").remove();
                $("#screenshot-mark").css({'display':'none'});
            });
    });
});