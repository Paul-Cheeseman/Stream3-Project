$(document).ready(function() { 


    //Highlight table rows for user to see active row
    $('#table-row-highlight tr').hover(function() {
            //Change cursor to pointing finger to make it clear to user that they can click anywhere on row
            $(this).css('cursor','pointer');
            //Highlight active row for user
            $(this).addClass("row-orange");
            $(this).siblings().removeClass("row-orange");
        });

    //enable highlighted row (see above) to be selected by user
    $('#table-row-highlight tr').click(function() {
        // Some JS to call page from product table row
        window.location.href = "/products/detail/?product_name=" + $(this).children(":first").text();

    });





});

