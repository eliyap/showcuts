
$(document).ready(function () {
    /* Set sidenav margin to 0px */
    function openNav() {
        $("#mySidenav").removeClass("closed").addClass("opened");
    }
    
    /* Set sidenav width to -250px */
    function closeNav() {
        $("#mySidenav").removeClass("opened").addClass("closed");
    }

    $("#open").click(openNav)
    $("#open-fixed").click(openNav)
    $("#close").click(closeNav)

    // Store references outside event handler:
    let $window = $(window);
    let $sidebar = $(mySidenav);
    
    function checkWidth() {
        let windowsize = $window.width();
        if ($("#mySidenav").hasClass("hidden")) {
            $("#open").addClass("always-on")
            $("#close").addClass("always-on")
        }
        else {
            if (windowsize > 768) {
                $("#mySidenav").removeClass("closed").addClass("opened");
                $("#SCtitle").removeClass("no-sidebar").addClass("with-sidebar");
            }
            else {
                $("#mySidenav").removeClass("opened").addClass("closed");
                $("#SCtitle").removeClass("with-sidebar").addClass("no-sidebar");
            }
        }
    }
    checkWidth();// Execute on load
    $(window).resize(checkWidth)// Bind event listener
    $("#id_iCloudLink").focus()// place cursor (on form page)


    // Magic Variable Toggle
    let output_shown = false;
    function toggleOutput(){
        if (output_shown){
            $(".output").removeClass("shown").addClass("hidden");
            output_shown = false;
        }
        else{
            $(".output").removeClass("hidden").addClass("shown");
            output_shown = true;
        }
    }
    
    $("#show-magic").click(toggleOutput)
    
    // Like Button AJAX
    $("#like").unbind('click').click(function toggleLike(){
        let elem = $(this);
        if (!elem.hasClass('disabled')){
            let likes = elem.next();
            let num_likes = parseInt(likes.text());
            let hxid = elem.attr("hxid");
            $.ajax({
                type:"GET",
                url:window.location.origin+"/share/like",
                data:{
                    hxid: hxid,
                },
                success: function (){
                    if (elem.hasClass("clicked")){
                        elem.removeClass("clicked");
                        likes.text(num_likes - 1);
                    }
                    else{
                        elem.addClass("clicked");
                        likes.text(num_likes + 1);
                    }
                }
            });
        }
    })
    // Save Button AJAX
    $("#save").unbind('click').click(function toggleSave(){
        let elem = $(this);
        if (!elem.hasClass('disabled')){
            let hxid = elem.attr("hxid");
            $.ajax({
                type:"GET",
                url:window.location.origin+"/share/save",
                data:{
                    hxid: hxid,
                },
                success: function (){
                    if (elem.hasClass("clicked")){
                        elem.removeClass("clicked");
                    }
                    else{
                        elem.addClass("clicked");
                    }
                }
            });
        }
    })
});
