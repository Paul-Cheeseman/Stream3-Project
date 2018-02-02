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


    //Enable text in dropdown menu to change to show the selection for this filter
    //To ensure that the selection is maintained between page reloads (ie each time *any* filter changes) the selection
    //is stored in the customers local storage. This jQuery sets value on screena and sets the value(s) in local storage.
    $(".dropdown-menu.gender li a").click(function(){
        $(".btn.gender:first-child").text($(this).text());
        $(".btn.gender:first-child").val($(this).text());
        $(".btn.gender").addClass("selected-filter"); 
        localStorage.setItem("gender", $(this).text());
    });
    $(".dropdown-menu.gender-xs li a").click(function(){
        $(".btn.gender-xs:first-child").text($(this).text().substring(0,1));
        $(".btn.gender-xs:first-child").val($(this).text().substring(0,1));
        $(".btn.gender-xs").addClass("selected-filter"); 
        localStorage.setItem("gender-xs", $(this).text().substring(0,1));
    });
    //As above, filter text change
    $(".dropdown-menu.age li a").click(function(){
        $(".btn.age:first-child").text($(this).text());
        $(".btn.age:first-child").val($(this).text());
        $(".btn.age").addClass("selected-filter");         
        localStorage.setItem("age", $(this).text());
    });
    $(".dropdown-menu.age-xs li a").click(function(){
        $(".btn.age-xs:first-child").text($(this).text().substring(0,2));
        $(".btn.age-xs:first-child").val($(this).text().substring(0,2));
        $(".btn.age-xs").addClass("selected-filter");         
        localStorage.setItem("age-xs", $(this).text().substring(0,2));
    });
    //As above, filter text change
    $(".dropdown-menu.size li a").click(function(){
        $(".btn.size:first-child").text($(this).text());
        $(".btn.size:first-child").val($(this).text());
        $(".btn.size").addClass("selected-filter");        
        localStorage.setItem("size", $(this).text());
    });
    //As above, filter text change
    $(".dropdown-menu.size-xs li a").click(function(){
        $(".btn.size-xs:first-child").text($(this).text().substring(0,1));
        $(".btn.size-xs:first-child").val($(this).text().substring(0,1));
        $(".btn.size-xs").addClass("selected-filter");        
        localStorage.setItem("size-xs", $(this).text().substring(0,1));
    });
    //As above, filter text change
    $(".dropdown-menu.colour li a").click(function(){
        $(".btn.colour:first-child").text($(this).text());
        $(".btn.colour:first-child").val($(this).text());
        $(".btn.colour").addClass("selected-filter");        
        localStorage.setItem("colour", $(this).text());
    });
    //As above, filter text change
    $(".dropdown-menu.colour-xs li a").click(function(){
        $(".btn.colour-xs:first-child").text($(this).text().substring(0,3));
        $(".btn.colour-xs:first-child").val($(this).text().substring(0,3));
        $(".btn.colour-xs").addClass("selected-filter");        
        localStorage.setItem("colour-xs", $(this).text().substring(0,3));
    });
    //As above, filter text change
    $(".dropdown-menu.category li a").click(function(){
        $(".btn.category:first-child").text($(this).text());
        $(".btn.category:first-child").val($(this).text());
        $(".btn.category").addClass("selected-filter");                 
        localStorage.setItem("category", $(this).text());
    });
    //As above, filter text change
    $(".dropdown-menu.category-xs li a").click(function(){
        $(".btn.category-xs:first-child").text($(this).text().substring(0,4));
        $(".btn.category-xs:first-child").val($(this).text().substring(0,4));
        $(".btn.category-xs").addClass("selected-filter");                 
        localStorage.setItem("category-xs", $(this).text().substring(0,4));
    });
    //As above, filter text change
    $(".dropdown-menu.price li a").click(function(){
        $(".btn.price:first-child").text($(this).text());
        $(".btn.price:first-child").val($(this).text());
        $(".btn.price").addClass("selected-filter");                 
        localStorage.setItem("price", $(this).text());
    });
   //As above, filter text change
    $(".dropdown-menu.ordering li a").click(function(){
        $(".btn.ordering:first-child").text($(this).text().substring(0,10));
        $(".btn.ordering:first-child").val($(this).text().substring(0,10));
        $(".btn.ordering").addClass("selected-filter");         
        localStorage.setItem("ordering", $(this).text().substring(0,10));
    });
    

    //To reset filters, local storage is cleared
    $(".resetall-products").click(function(){
        localStorage.removeItem("gender");
        localStorage.removeItem("gender-xs");        
        localStorage.removeItem("age");
        localStorage.removeItem("age-xs");        
        localStorage.removeItem("size");
        localStorage.removeItem("size-xs");        
        localStorage.removeItem("colour");
        localStorage.removeItem("colour-xs");        
        localStorage.removeItem("category");
        localStorage.removeItem("category-xs");        
        localStorage.removeItem("price");
        localStorage.removeItem("ordering");
    });


    //To ensure that the selection is maintained between page reloads (ie each time *any* filter changes) the selection
    //is stored in the customers local storage, this is retrieving the value(s)
    if (localStorage.getItem("gender") !== null){
        $(".btn.gender:first-child").text(localStorage.getItem("gender"));
        $(".btn.gender").addClass("selected-filter"); 
    }
    if (localStorage.getItem("gender-xs") !== null){
        $(".btn.gender-xs:first-child").text(localStorage.getItem("gender-xs"));
        $(".btn.gender-xs").addClass("selected-filter"); 
    }    
    if (localStorage.getItem("age") !== null){
        $(".btn.age:first-child").text(localStorage.getItem("age"));
        $(".btn.age").addClass("selected-filter");         
    }
    if (localStorage.getItem("age-xs") !== null){
        $(".btn.age-xs:first-child").text(localStorage.getItem("age-xs"));
        $(".btn.age-xs").addClass("selected-filter");         
    }    
    if (localStorage.getItem("size") !== null){
        $(".btn.size:first-child").text(localStorage.getItem("size"));
        $(".btn.size").addClass("selected-filter");        
    }    
    if (localStorage.getItem("size-xs") !== null){
        $(".btn.size-xs:first-child").text(localStorage.getItem("size-xs"));
        $(".btn.size-xs").addClass("selected-filter");        
    }    
    if (localStorage.getItem("colour") !== null){
        $(".btn.colour:first-child").text(localStorage.getItem("colour"));
        $(".btn.colour").addClass("selected-filter");                
    }    
    if (localStorage.getItem("colour-xs") !== null){
        $(".btn.colour-xs:first-child").text(localStorage.getItem("colour-xs"));
        $(".btn.colour-xs").addClass("selected-filter");                
    }    
    if (localStorage.getItem("category") !== null){
        $(".btn.category:first-child").text(localStorage.getItem("category"));
        $(".btn.category").addClass("selected-filter");        
    }
    if (localStorage.getItem("category-xs") !== null){
        $(".btn.category-xs:first-child").text(localStorage.getItem("category-xs"));
        $(".btn.category-xs").addClass("selected-filter");        
    }
    if (localStorage.getItem("price") !== null){
        $(".btn.price:first-child").text(localStorage.getItem("price"));
        $(".btn.price").addClass("selected-filter");        
    }
    if (localStorage.getItem("ordering") !== null){
        $(".btn.ordering:first-child").text(localStorage.getItem("ordering"));
        $(".btn.ordering").addClass("selected-filter");                 
    }
});

