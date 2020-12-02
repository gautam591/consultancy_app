
$(document).ready(function(){
    $(document).on('click','.searchQueryButton',function(){
        //console.log("Button Pressed : Submit Post");
        document.getElementById('overlapContentPage').style.display='block';
        document.getElementById('axisMenu').style.display='none';
        document.body.style.overflow = "hidden";
        document.getElementById("axisNavbar").style.top = "0";
        let search_query =  $('#search_query_input').val();
        //console.log("clicked : ",fd)
          $.ajax({
              type:'GET',
              url:getBaseURLs('searchURL'),
              data: {'searchQuery':search_query},
              success:function(response){
                    $(".overlapContentPage").append(response);                
               },
              error: function(response) {
                alert("Something Went Wrong. Try Again !!")
              }
          });
       });
  
  });
function searchClicker(){
    $('.searchQueryButton').click();
};

  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });


  
