function notify(glyph, txt) {
    $("#notify").css({ 'top': '1rem' });
    $("#notify img").css({ 'display': 'none' });
    glyph.css({ 'display': 'inline-block' });
    $("#notify span").text(txt);
    setTimeout(function () {
        $("#notify").css({ 'top': '-3rem' });
    }, 2000);
}
