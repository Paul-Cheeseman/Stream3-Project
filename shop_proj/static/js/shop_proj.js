$(document).ready(function() {

    $('#logout_btn').click(function() {
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

                    setTimeout(function() {
                        console.log("Triggered");
                        window.location.href = "/accounts/logout/?cart_store=yes";
                    }, 3500);
                } else {
                    swal("Shazam! You cart has been deleted", {
                        icon: "error",
                    });

                    setTimeout(function() {
                        window.location.href = "/accounts/logout/?cart_store=no";
                    }, 3500);
                }
            });
    });
});