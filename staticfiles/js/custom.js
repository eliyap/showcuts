/* Set sidenav margin to 0px */
function openNav() {
    $("#mySidenav").removeClass("closed").addClass("opened");
}

/* Set sidenav width to -250px */
function closeNav() {
    $("#mySidenav").removeClass("opened").addClass("closed");
}

$(document).ready(function () {
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
});
