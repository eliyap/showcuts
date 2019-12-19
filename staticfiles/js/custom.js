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

    let $window = $(window);

    function checkWidth() {
        let windowsize = $window.width();
        if ($("#mySidenav").hasClass("hidden")) {
            $("#open").addClass("always-on");
            $("#close").addClass("always-on");
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
    $(window).resize(checkWidth);// Bind event listener
    $("#id_iCloudLink").focus();// place cursor (on form page)
    $("#id_subreddit").focus();// place cursor (on form page)


    // Magic Variable Toggle
    let output_shown = false;

    $("#show-magic").click(function toggleOutput() {
        if (output_shown) {
            $(".output").removeClass("shown").addClass("hidden");
            output_shown = false;
        }
        else {
            $(".output").removeClass("hidden").addClass("shown");
            output_shown = true;
        }
    });

    // Like Button AJAX
    function toggleLike() {
        let elem = $(this);
        // alert('hi!');
        let likes = elem.next();
        let num_likes = parseInt(likes.text());
        let hxid = elem.attr("hxid");
        $.ajax({
            type: "GET",
            url: window.location.origin + "/share/like",
            data: {
                hxid: hxid,
            },
            success: function () {
                if (elem.hasClass("clicked")) {
                    elem.removeClass("clicked");
                    likes.text(num_likes - 1);
                }
                else {
                    elem.addClass("clicked");
                    likes.text(num_likes + 1);
                }
            }
        });
    }
    $("#like").unbind('click').click(toggleLike)
    $(".like-btn").unbind('click').click(toggleLike)
    // Save Button AJAX
    $("#save").unbind('click').click(function toggleSave() {
        let elem = $(this);
        let hxid = elem.attr("hxid");
        $.ajax({
            type: "GET",
            url: window.location.origin + "/share/save",
            data: {
                hxid: hxid,
            },
            success: function () {
                if (elem.hasClass("clicked")) {
                    elem.removeClass("clicked");
                }
                else {
                    elem.addClass("clicked");
                }
            }
        });
    })
    $("#xpost,#info").unbind('click').click(function () {
        let elem = $(this);
        if (elem.hasClass("clicked")) {
            elem.removeClass("clicked");
        }
        else {
            elem.addClass("clicked");
        }
    });

    // account deletion warning
    $("#safety-glass").unbind('click').click(function () {
        let elem = $(this);
        $("#disconnect-warning").addClass("show");
        $("h1,h2,h3,h4,h5,h6,p,form").addClass("blurred");
        elem.hide();
    });

    $("#accept-delete").unbind('click').click(function () {
        $("#disconnect-warning").removeClass("show");
        $(".blurred").removeClass("blurred");
    });

    $("#icloud-submit").click(function () {
        $(this).addClass("clicked");
    })
});

// loading animation
$(window).bind('beforeunload', function () {
    if ($("#icloud-submit").hasClass('clicked')) {
        $("#loading").css({ 'display': 'block', 'opacity': '100%' });
    }
});

