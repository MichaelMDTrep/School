function footerPosition() {
    var windowHeight = $(window).height();
    var documentHeight = $(document).height();
    if (documentHeight == windowHeight) {
        $(".footer").css({'position': 'absolute', 'bottom': '0px', 'width': '100%'});
    } else {
        $(".footer").css({'position': '', 'bottom': '', 'width': ''});
    }
}

$(document).ready(function() {
    footerPosition();
})

$(window).resize(function() {
    footerPosition();
})