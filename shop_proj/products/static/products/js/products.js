$(document).ready(function() { 


    $('#table-row-highlight tr').hover(function() {
            //Change cursor to pointing finger to make it clear to user that they can click anywhere on row
            $(this).css('cursor','pointer');
            //Highlight active row for user
        	$(this).addClass("row-gray");
        }, function() {
            //Remove active row highlight when row not hovered over
        	$(this).removeClass("row-gray");
    });

    $('#table-row-highlight tr').click(function() {
		// Some JS to call page from product table row
        window.location.href = "/products/detail/?product_name=" + $(this).children(":first").text();

    });


    /* This functionality is nice, but does rely on hardcoding values which introduces a maintenace
       overhead and the potential for mistakes/errors. Given the small scope of this site and the nice
       impression for customer it is being kept in, but should be reviewed if site is expected to 
       support a wider range of products */

    $(".dropdown-menu li a").click(function () {
        console.log("dropdown menu triggered");
        var selText = $(this).text();
        
        if (selText == "Male" || selText == "Female"){
            $(".gender-selection").removeClass("caret");
            $(".gender-selection").html(selText);
        }
        else if (selText == "Adult" || selText == "Child"){
            $(".age-selection").removeClass("caret");
            $(".age-selection").html(selText);
        }
        else if (selText == "Small" || selText == "Medium" || selText == "Large"){
            $(".size-selection").removeClass("caret");
            $(".size-selection").html(selText);
        }
        else if (selText == "Red" || selText == "Yellow" || selText == "Pink" || selText == "Blue" || selText == "Purple" || selText == "Orange" || selText == "Green" || selText == "Black" || selText == "White"){
            $(".colour-selection").removeClass("caret");
            $(".colour-selection").html(selText);
        }
    });

});


    function URLclean(){
        console.log("working?");
        if (window.location.href.indexOf('?') > -1) {
            window.location.href = window.location.pathname;
        }
    }


