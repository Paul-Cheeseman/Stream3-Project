$(document).ready(function() {


	//Detect logout button click
    $('#logout_btn_save').click(function() {
        $(this).data('clicked', true);
    });


    //Detect if the browser back button has been pressed, if so warn users that results may confuse them
    window.history.pushState('', null, './');
    $(window).on('popstate', function() {

        if ($('#logout_btn_save').data('clicked')) {
            //Do nothing, this is to prevent the alert below interfering with the default logout JQuery
        } else {
            window.alert("Please navigate from this page using the site menu rather than browser navigation buttons to ensure a quality user experience");
        }
    })

});