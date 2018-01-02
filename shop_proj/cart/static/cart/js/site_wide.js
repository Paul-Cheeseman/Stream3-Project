$(document).ready(function() {


    /*  This code needs to be put in the generic project app if it is to be applied to logout. 
        This is on the assumption that logout will be used on each page, the code is kepted 
        commented out here so that it stays with the app, even when it is imported, and uncommented!, 
        in the main project static JS file 


        Kept in a seperate file to clearly delinate between code that needs to be site wide and code 
        in cart.js that can be local to the app.
    */



    /* 
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
    */
    
});