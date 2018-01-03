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

/*
  $(".dropdown-menu li a").click(function(){
    window.alert("Hi");
    //$(".btn:first-child").text($(this).text());
    //$(".btn:first-child").val($(this).text());
  });
*/

    $(".dropdown-menu.gender li a").click(function(){
        $(".btn.gender:first-child").text($(this).text());
        $(".btn.gender:first-child").val($(this).text());
        localStorage.setItem("gender", $(this).text());
    });


    $(".dropdown-menu.age li a").click(function(){
        $(".btn.age:first-child").text($(this).text());
        $(".btn.age:first-child").val($(this).text());
        localStorage.setItem("age", $(this).text());
    });


    $(".btn.resetall").click(function(){
        localStorage.removeItem("gender");
        localStorage.removeItem("age");
    });


    if (localStorage.getItem("gender") !== null){
        $(".btn.gender:first-child").text(localStorage.getItem("gender"));
    }
    if (localStorage.getItem("age") !== null){
        $(".btn.age:first-child").text(localStorage.getItem("age"));
    }

});

