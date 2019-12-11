$(document).ready(function () {
    $("#screenshot").click(function () {
        domtoimage.toBlob(document.getElementById('action-container')) // cannot be turned into jQuery, I already tried.
            .then(function (blob) {
                window.saveAs(blob, $(document).attr('title')+'.png');
            });
    })
});
