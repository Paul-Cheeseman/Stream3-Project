$(document).ready(function() {

	/*  This code has been imported from the Cart App, but needs to be here for ease of access for
		all the pages. Trying to reference the code when it is within the Cart App ststic file 
		gets rather confusing with STATIC file references (trying to call the JS file from within 
		Carts STATIC dir from a template (main) which is referencing a site wide STATIC dir. */

	$('#logout_btn').click(function() {
        window.location.href = "/accounts/logout/?cart_store=no";
    });


    $('#logout_btn_save').click(function() {
        //This is for alert/confirmation box for deleting cart
        //It is based on code from: https://sweetalert.js.org/guides/
        swal({
                title: "Cart Deletion",
                text: "Would you like to save your cart for the next time you log in?",
                icon: "warning",
                buttons: true,
                //dangerMode: true,
            })
            .then((willDelete) => {
                if (willDelete) {
                    swal("Your cart has been stored!", {
                        icon: "success",
                    });

                    //setTimeout(function() {
                    //    console.log("Triggered");
                    window.location.href = "/accounts/logout/?cart_store=yes";
                    // }, 3500);
                } else {
                    swal("Shazam! You cart has been deleted", {
                        icon: "error",
                    });

                    //setTimeout(function() {
                    window.location.href = "/accounts/logout/?cart_store=no";
                    //}, 3500);
                }
            });
    });


    /*
        This is a required duplicate of jQuery from the Products app, so the filter bar gets reset to default when the 
        products menu link clicked.
    */
    $(".resetall-products").click(function(){
        localStorage.removeItem("gender");
        localStorage.removeItem("age");
        localStorage.removeItem("ordering");
        localStorage.removeItem("price");
        localStorage.removeItem("category");
        localStorage.removeItem("colour");
        localStorage.removeItem("size");
    });

});



     //For Google Maps
     function initMap() {
        var fleet = {lat: 50.7879964, lng: -1.0840458};
         var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 14,
            center: fleet 
        });
        var marker = new google.maps.Marker({
            position: fleet,
            map: map
        });
     }