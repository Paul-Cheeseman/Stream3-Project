$(document).ready(function() { 
     console.log("running");

    $('#table-row-highlight tr').hover(function() {
        	console.log("Hovering over table row");
        	$(this).addClass("row-gray");
        }, function() {
        	console.log("Not over table row");
        	$(this).removeClass("row-gray");
        	//$(this).removeClass("testgray");
    });
    

    $('#table-row-highlight tr').click(function() {
        console.log($(this).children(":first").text());

		// Some JS to call page from table row
		window.location.href = "/product_detail/?product_name=" + $(this).children(":first").text();
    });





});