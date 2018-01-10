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
        window.location.href = "/products/detail/?product_name=" + $(this).children(":first").text();

    });


    $(".dropdown-menu.gender li a").click(function(){
        $(".btn.gender:first-child").text($(this).text());
        $(".btn.gender:first-child").val($(this).text());
        $(".btn.gender").addClass("selected-filter"); 
        localStorage.setItem("gender", $(this).text());
    });


    $(".dropdown-menu.age li a").click(function(){
        $(".btn.age:first-child").text($(this).text());
        $(".btn.age:first-child").val($(this).text());
        $(".btn.age").addClass("selected-filter");         
        localStorage.setItem("age", $(this).text());
    });


    $(".dropdown-menu.ordering li a").click(function(){
        $(".btn.ordering:first-child").text($(this).text());
        $(".btn.ordering:first-child").val($(this).text());
        $(".btn.ordering").addClass("selected-filter");         
        localStorage.setItem("ordering", $(this).text());
    });


    $(".dropdown-menu.price li a").click(function(){
        $(".btn.price:first-child").text($(this).text());
        $(".btn.price:first-child").val($(this).text());
        $(".btn.price").addClass("selected-filter");                 
        localStorage.setItem("price", $(this).text());
    });

    $(".dropdown-menu.category li a").click(function(){
        $(".btn.category:first-child").text($(this).text());
        $(".btn.category:first-child").val($(this).text());
        $(".btn.category").addClass("selected-filter");                 
        localStorage.setItem("category", $(this).text());
    });


    $(".dropdown-menu.colour li a").click(function(){
        $(".btn.colour:first-child").text($(this).text());
        $(".btn.colour:first-child").val($(this).text());
        $(".btn.colour").addClass("selected-filter");        
        localStorage.setItem("colour", $(this).text());
    });

    $(".dropdown-menu.size li a").click(function(){
        $(".btn.size:first-child").text($(this).text());
        $(".btn.size:first-child").val($(this).text());
        $(".btn.size").addClass("selected-filter");        
        localStorage.setItem("size", $(this).text());
    });



    $(".resetall-products").click(function(){
        localStorage.removeItem("gender");
        localStorage.removeItem("age");
        localStorage.removeItem("ordering");
        localStorage.removeItem("price");
        localStorage.removeItem("category");
        localStorage.removeItem("colour");
        localStorage.removeItem("size");
    });



    if (localStorage.getItem("gender") !== null){
        $(".btn.gender:first-child").text(localStorage.getItem("gender"));
        $(".btn.gender").addClass("selected-filter"); 
    }
    if (localStorage.getItem("age") !== null){
        $(".btn.age:first-child").text(localStorage.getItem("age"));
        $(".btn.age").addClass("selected-filter");         
    }
    if (localStorage.getItem("ordering") !== null){
        $(".btn.ordering:first-child").text(localStorage.getItem("ordering"));
        $(".btn.ordering").addClass("selected-filter");                 
    }
    if (localStorage.getItem("price") !== null){
        $(".btn.price:first-child").text(localStorage.getItem("price"));
        $(".btn.price").addClass("selected-filter");        
    }
    if (localStorage.getItem("category") !== null){
        $(".btn.category:first-child").text(localStorage.getItem("category"));
        $(".btn.category").addClass("selected-filter");        
    }
    if (localStorage.getItem("colour") !== null){
        $(".btn.colour:first-child").text(localStorage.getItem("colour"));
        $(".btn.colour").addClass("selected-filter");                
    }    
    if (localStorage.getItem("size") !== null){
        $(".btn.size:first-child").text(localStorage.getItem("size"));
        $(".btn.size").addClass("selected-filter");        
    }    

});

