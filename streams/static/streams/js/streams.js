function getMonth(month) {
    if (month == 'last_month') {
        // tab
        $('.stream-tab-last-month').addClass('active');
        $('.stream-tab-this-month').removeClass('active');
        // content
        $('.previous-month').fadeIn().removeClass('d-none');
        $(".present-month").fadeOut().addClass("d-none");
    }
    else if (month == 'this_month') {
        // tab
        $('.stream-tab-last-month').removeClass('active');
        $('.stream-tab-this-month').addClass('active');
        // content
        $('.previous-month').fadeOut().addClass('d-none');
        $(".present-month").fadeIn().removeClass("d-none");
    }
}