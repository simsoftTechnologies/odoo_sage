$(document).ready(function () {
 
    $( ".toggle_leftmenu").click(function() {
            $( ".o_sub_menu").animate({
            width: 'toggle'
        });
            $( ".o_sub_menu").find('img').animate({
            width: 'toggle'
        });

    });
    
    $( "ul.nav li a" ).each(function(index) {
        $(this).on("click", function(){
            $( ".o_sub_menu").show();
            $( ".o_sub_menu").find('img').show();
        }); 
    });

    $("#toggle-menu").click(function(e) {
        e.preventDefault();
        $(".dashboard-wrapper").toggleClass("activeclass");
});
});

