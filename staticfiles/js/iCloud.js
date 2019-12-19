$(document).ready(function () {
    $("#icloud-copy").unbind('click').click(function () {
        const elem = $("#iCloud-txt");
        elem.focus();
        elem.select();
        document.execCommand("copy");
        notify($("#nf-copy"), 'Copied');

        $("#icloud").removeClass('clicked');
    });
    $("#icloud-qr").unbind('click').click(function () {
        var w = window.open();
        var html = $("#qrcode").html();

        $(w.document.body).html(html);
        $("#icloud").removeClass('clicked');
    });
    $("#icloud-link").unbind('click').click(function () {
        $("#icloud").removeClass('clicked');
    });
});
