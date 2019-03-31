// // Scroll to specific values
// // scrollTo is the same
// window.scroll({
//     top: 0,
//     left: 0,
//     behavior: 'smooth'
// });

// // Scroll certain amounts from current position 
// window.scrollBy({
//     top: 100, // could be negative value
//     left: 0,
//     behavior: 'smooth'
// });

// // Scroll to a certain element
// document.querySelector('.hello').scrollIntoView({
//     behavior: 'smooth'
// });
if ($('#back-to-top').length) {
    var scrollTrigger = 100, // px
        backToTop = function () {
            var scrollTop = $(window).scrollTop();
            if (scrollTop > scrollTrigger) {
                $('#back-to-top').addClass('show');
            } else {
                $('#back-to-top').removeClass('show');
            }
        };
    backToTop();
    $(window).on('scroll', function () {
        backToTop();
    });
    $('#back-to-top').on('click', function (e) {
        e.preventDefault();
        $('html,body').animate({
            scrollTop: 0
        }, 700);
    });
}