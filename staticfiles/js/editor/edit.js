function edit_input(globals, thing) {

    function dump_magic(element) {
        /* dumps <span> as a magic variable string, saves the magic variables' details */

        let prev = element.prev();
        let name = element.text().replace('‎', '');
        let magicDict = { // stores magic var data
            UUID: "",
        };
        if (!prev.is("img")) { return name; }

        // has image -> must be magic var
        let glyph = prev.attr("src").replace(/.*?\/cat\//, '');  // get last part of image path
        magicDict.UUID = prev.attr("UUID");
        if (magicDict.UUID === "None") { // no UUID -> must be a system var
            switch (glyph) {
                case "Clipboard.svg":
                    return '$(Clipboard)';
                case "Input.svg":
                    return '$(Shortcut Input)';
                case "Date.svg":
                    return '$(Current Date)';
                case "Ask.svg":
                    return '$(Ask Each Time)';
                default: return '$(UNKNOWN)';
            }
        }

        // store magic var data
        magicDict.name = name;
        magicDict.glyph = glyph;
        window.magic.push(magicDict);
        return `$(${name})`;
    }

    let text = '';
    $("span[field]").unbind(); // block other fields. reconsider why?
    thing.children('span').each(
        function () { text += dump_magic($(this)); }  // $(this) refers to child <span>
    );

    // if registered as 'empty', clear out placeholder text
    if (thing.hasClass('empty')) {
        thing.removeClass('empty');
        text = '';
    };

    thing.html( // place input field
        $('<input></input>')
            .attr({
                'name': 'magic_input',
                'id': 'magic_input',
                'value': text,
            })
            .css({
                "width": "5rem",
            })
            .val(text)
    );

    $('#magic_input').focus(); // place cursor inside input
    globals.saved = false;
};

function save_input(globals) {
    function parse_magic(magic_str, parent) {
        /* breaks down magic strings */
        let magic_re = /(.*?)(\$\(.+?\))/i;
        var fstr = "";
        var match = 1;

        while (match) {
            match = null;
            if (magic_str.match(magic_re)) { // find magic vars, if none exist, move on.
                match = magic_str.match(magic_re);
                fstr += spanWrap(match[1]) + load_magic(match[2], parent);
                magic_str = magic_str.replace(magic_re, '');
            }
        }
        fstr += spanWrap(magic_str);
        return fstr;
    }

    function load_magic(name, parent) {
        /* loads variable from magic table */
        name = name.substring(2, name.length - 1); // remove the $()
        // check if the name exists in the global scope
        let matches = window.magic.filter(md => md.name.toUpperCase() === name.toUpperCase()); // case insensitive.
        if (matches.length) {
            let chosen = matches[0]; // TODO: make a better selector
            return magicWrap(chosen.name, chosen.UUID, chosen.glyph);
        }

        // system variables
        switch (name) {
            case "Clipboard":
                return magicWrap(name, 'None', 'Clipboard.svg');
            case "Shortcut Input":
                return magicWrap(name, 'None', 'input.svg');
            case "Current Date":
                return magicWrap(name, 'None', 'Date.svg');
            case "Ask Each Time":
                return magicWrap(parent.attr("ask_each_time"), 'None', 'Ask.svg');
        }
    }

    function parse_input(input) {

        let magic_str = input.val();
        let parent = input.parent();
        let blank_text = parent.attr('blank_text');
        let deflt = parent.attr('default');

        if (magic_str === '') { // use provided default or blank text
            return spanWrap(blank_text ? blank_text : (deflt ? deflt : "EMPTY")); // "EMPTY" should not be triggered. add error?
        }
        try { // parse magic string
            return $(parse_magic(magic_str, parent));
        }
        catch (err) { // problem parsing magic vars, don't save!
            // error handling here
            throw err; // DEBUG
        }
    };

    if (!globals.saved) {
        globals.saved = true; // change flag BEFORE removal, as .remove() triggers `blur` again.
        let input = $('#magic_input').first();
        parse_input(input).appendTo($('#magic_input').parent());
        $('#magic_input').remove();
        $("span[field='number']").click(function (event) {
            edit_input(globals, $(event.currentTarget)); // pass as a JS object, coerced using $()
        });
    }
};

function spanWrap(content) {
    // return nothing if content is empty
    return content != '' ? `<span>${content}</span>` : "";
}
function magicWrap(content, UUID, glyph) {
    let assetStr = "/static/assets/cat/"; // could be something else
    return `<img class="inline-glyph" src="${assetStr}${glyph}" UUID="${UUID}"/><span>&lrm;${content}</span>`;
}
export { edit_input, save_input };