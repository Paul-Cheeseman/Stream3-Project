$(document).ready(function() {

	/*
		jQuery to highlight the active row on a table so that the user can see the active row.
	*/
    $('#table-row-highlight tr').hover(function() {
            //Change cursor to pointing finger to make it clear to user that they can click anywhere on row
            $(this).css('cursor','pointer');
            //Highlight active row for user
            $(this).addClass("row-orange");
        }, function() {
            //Remove active row highlight when row not hovered over
            $(this).removeClass("row-orange");
    });

   
});