

$(document).ready(function () {
    /*
    $(function() {
        $.contextMenu({
            selector: "span[field='number']", 
            callback: function(key, options) {
                var m = "clicked: " + key;
                window.console && console.log(m) || alert(m); 
            },
            items: {
                "edit": {name: "Edit", icon: "edit"},
                "cut": {name: "Cut", icon: "cut"},
               copy: {name: "Copy", icon: "copy"},
                "paste": {name: "Paste", icon: "paste"},
                "delete": {name: "Delete", icon: "delete"},
                "sep1": "---------",
                "quit": {name: "Quit", icon: function(){
                    return 'context-menu-icon context-menu-icon-quit';
                }}
            }
        });

        $("span[field='number']").on('click', function(e){
            console.log('clicked', this);
        })    
    });
    */

    function edit_input() {
        $("span[field='number']").unbind();
        field = $(this).attr('field')
        text = ''
        $(this).children('span').each(
            function () {
                text += $(this).text().replace('‎', ''); //CONTAINS &lrm;
            }
        )
        if ($(this).hasClass('empty')) {
            $(this).removeClass('empty');
            text = '';
        };
        $(this).html('');
        $('<input></input>')
            .attr({
                'type': function () {
                    switch (field) {
                        case 'number':
                            return 'number';
                        default:
                            return 'text';
                    }
                }(),
                'name': 'fname',
                'id': 'magic_input',
                // 'size': '30',
                'value': text,
            })
            .appendTo($(this));
        $('#magic_input').focus();
        saved = false;
    }
    $("span[field='number']").click(edit_input);

    function save_input() {
        if (!saved) {
            saved = true; // change flag BEFORE removal, removal triggers `blur`.
            text = $('#magic_input').val();
            $('<span>' + text + '</span>')
                .appendTo($('#magic_input').parent());
            $('#magic_input').remove();
            $("span[field='number']").click(edit_input);
        }
    };

    $(document).on('blur', '#magic_input', save_input);

    $("input").keydown(function () {
        $("input").css("background-color", "yellow");
    });

    $(document).keydown(function (e) {
        if (e.which == 13) {
            save_input();
        }
    });
    var saved = true;
});