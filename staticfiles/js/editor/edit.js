function edit_input(globals, thing) {
    $("span[field='number']").unbind();
    let field = function (field) {
        switch (field) {
            case 'number':
                return 'number';
            default:
                return 'text';
        }
    }(thing.attr('field'));
    let text = '';
    thing.children('span').each(
        function () { // $(this) refers to each child <span>
            text += dump_magic($(this)); //CONTAINS &lrm;
        }
    );
    

    // if registered as 'empty', clear out placeholder text
    if (thing.hasClass('empty')) {
        thing.removeClass('empty');
        text = '';
    };

    // place input field
    thing.html('');
    $('<input></input>')
        .attr({
            // 'type': field,
            'name': 'magic_input',
            'id': 'magic_input',
            'value': text,
        })
        .css({
            "width": "5rem",
        })
        .val(text)
        .appendTo(thing);
    // place cursor inside input
    $('#magic_input').focus();
    globals.saved = false;
};

function save_input(globals) {
    if (!globals.saved) {
        globals.saved = true; // change flag BEFORE removal, as .remove() triggers `blur` again.
        let input = $('#magic_input').first();
        parse_input(input).appendTo($('#magic_input').parent());
        $('#magic_input').remove();
        $("span[field='number']").click(function(event){
            edit_input(globals, $(event.currentTarget)); // pass as a JS object, coerced using $()
        });
    }
};

function parse_input(input){
    let magic_str = input.val();
    let parent = input.parent();
    let blank_text = parent.attr('blank_text');
    let deflt = parent.attr('default');

    if (magic_str === ''){
        if (blank_text){
            parent.addClass('empty');
            return $('<span>' + blank_text + '</span>');
        }
        else if (deflt){
            return $('<span>' + deflt + '</span>');
        }
    }
    else{
        try{
            parse_magic(magic_str);
        }
        catch (err){ // problem parsing magic vars, don't save!

        }
    }
    return $('<span>' + input.val() + '</span>');
};

function parse_magic(magic_str){
    let magic_re = /(.*?)(\$\([\w|\s]+?\))/i;
    var fstr = [];
    var match = 1;
    
    while(match){
        match = null;
        if (magic_str.match(magic_re)){ // find magic vars, if none exist, move on.
            match = magic_str.match(magic_re);
            fstr.push(match[1], match[2]);
            magic_str = magic_str.replace(magic_re, '');
        }
    }
    fstr.push(magic_str);
    console.log(fstr);
}

/*
dumps each <span> as text, or an appropriate magic variable string.
also extracts and saves the details of the magic variable as a JS object.
*/
function dump_magic(element){
    let prev = element.prev();
    let name = element.text().replace('‎', '');
    var magic = { // stores magic var data
        type:"",
        UUID:"",
    };
    if (prev.is("img")){ // has image -> must be magic var
        let ga = prev.attr("src").split("/");
        let glyph = ga[ga.length - 1]; // get last part of image path
        magic.UUID = prev.attr("UUID");
        if (magic.UUID === "None"){ // no UUID -> must be a system var
            switch (glyph){
                case "Ask.svg": return '$(Ask Each Time)';
                case "Clipboard.svg": return '$(Clipboard)';
                case "Input.svg": return '$(Shortcut Input)';
                case "Date.svg": return '$(Current Date)';
                default: return '$(UNKNOWN)';
            }
        }
        else{
            // TODO: put something here to store the variable data...
            return `$(${name})`;
        }
    }
    else return name;
    // check for Clipboard, Ask Each Time, etc.
    // check for standard magic vars (include UUID data, etc.)
}

function load_magic(name){
    name = name.substring(1,name.length()-2);
    return name;
}
export {edit_input, save_input};