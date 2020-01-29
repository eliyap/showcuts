import {edit_input, save_input} from "./editor/edit.js";


$(document).ready(function () {
    let globals = { // values may be manipulated by reference
        saved:true,
    }

    
    $("span[field='number']").click(function(event){
        edit_input(globals, $(event.currentTarget)); // pass as a JS object, coerced using $()
    });
    $(document).on('blur', '#magic_input', function(){
        save_input(globals);
    });

    $("input").keydown(function () {
        $("input").css("background-color", "yellow");
    });

    $(document).keydown(function (e) {
        if (e.which == 13) {
            save_input(globals);
        }
    });
});