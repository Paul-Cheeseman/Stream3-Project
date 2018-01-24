$(document).ready(function() { 


    $('#table-row-highlight tr').hover(function() {
            //Change cursor to pointing finger to make it clear to user that they can click anywhere on row
            $(this).css('cursor','pointer');
            //Highlight active row for user
        	$(this).addClass("row-orange");
        }, function() {
            //Remove active row highlight when row not hovered over
        	$(this).removeClass("row-orange");
    });

    $('#table-row-highlight tr').click(function() {
		// Some JS to call page from product table row
        window.location.href = "/orders/detail/?id=" + $(this).find('.order_id').text();
        //console.log($(this).find('.order_id').text());

        


    });





});

