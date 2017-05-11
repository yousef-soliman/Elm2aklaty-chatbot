function newMessageFromUser(textMessage){
  var ulElement = document.getElementById("chatList");
  var li =document.createElement("LI")
  li.innerHTML = "<span class='chat-img pull-left'><img class='img usr' src='static/img/user_3.jpg' alt='User Avatar'></span><div class='chat-body clearfix'><div class='header'><strong class='primary-font'>John Doe</strong><small class='pull-right text-muted'><i class='fa fa-clock-o'></i> 12 mins ago</small></div><p>"+textMessage+"</p></div>"
  li.className = "left clearfix";
  li.scrollIntoView();
  ulElement.appendChild(li);
  window.scrollTo(0, document.getElementById("chatBody").scrollHeight);

}

function newMessageFromChat(textMessage){
  var ulElement = document.getElementById("chatList");
  var li =document.createElement("LI")
  li.innerHTML = "<span class='chat-img pull-right'><img class='img usr' src='static/img/user_1.jpg' alt='User Avatar'></span><div class='chat-body clearfix'><div class='header'><strong class='primary-font'>John Doe</strong><small class='pull-right text-muted'><i class='fa fa-clock-o'></i> 12 mins ago</small></div><p>"+textMessage+"</p></div>"
  li.className = "right clearfix";
  ulElement.appendChild(li);
  //window.scrollTo(0, document.getElementById("chatBody").scrollHeight);
  li.scrollIntoView();
}
function send(e) {
  $.post('/getrestaurant', {
        text: $(e).text()
        
    }).done(function(data) {
      for(var i in data["path"]){
          newMessageFromChat("<img class='menu' src = ' "+ data["path"][i] +"' />")
      }
      for(var i in data["buttons"]){
          addButton(data["buttons"][i])
      }
    }).fail(function() {
        alert("d")
    });
}

$(document).ready(function(){
    $("#allrestaurants").click(function(){
        newMessageFromUser("كل المطاعم");
        $.get("http://localhost:5000/allrestaurants", function(data){
            newMessageFromChat(data["message"])
            for(var i in data["buttons"]){
              addButton(data["buttons"][i])
            }
        });
    });
    $("#wanttoeat").click(function(){
        newMessageFromUser("عايز اكل");
        $.get("http://localhost:5000/wanttoeat", function(data){
            newMessageFromChat(data["message"])
            for(var i in data["buttons"]){
              addButton(data["buttons"][i])
            }
        });
    });
});

function getmenu(){
  newMessageFromUser($(e).text());
  $.post('/getmenu', {
        text: $(e).attr('name')
        
    }).done(function(data) {
      
    }).fail(function() {
        alert("d")
    });
}

function getcategory(e){
  newMessageFromUser($(e).text());
  $.post('/getcategory', {
        text: $(e).attr('name')
        
    }).done(function(data) {
      newMessageFromChat(data["message"])
      for(var i in data["buttons"]){
          addButton(data["buttons"][i])
      }
    }).fail(function() {
        alert("d")
    });
}


function addButton(json_str){
  var x = document.getElementsByTagName("UL");
  button = document.createElement("button");
  button.innerHTML = json_str["text"];
  button.setAttribute("onclick",json_str["do"]);
  button.setAttribute("name",json_str["name"]);
  button.setAttribute("class","btn button");
  //button.setAttribute("class","tag")
  x[0].appendChild(button);
  button.scrollIntoView();
}

function good(){
  newMessageFromChat("بالهنا و والشفا :D")
}

function ok(){
  if(ismarked){
    $.get("http://localhost:5000/category", function(data){
          newMessageFromChat(data["message"])
          for(var i in data["buttons"]){
            addButton(data["buttons"][i])
          }
    });
  }
  else{
    $.get("http://localhost:5000/wanttoeat", function(data){
            newMessageFromChat(data["message"])
            for(var i in data["buttons"]){
              addButton(data["buttons"][i])
            }
        });
  }

}

var marker=null ;
var ismarked = false;
var map;
// var im = 'http://www.robotwoods.com/dev/misc/bluecircle.png';
function locate(){
    navigator.geolocation.getCurrentPosition(initialize,fail);
}

function initialize(position) {
    
    newMessageFromUser("حدد مكاني");
    var ulElement = document.getElementById("chatList");
    var li =document.createElement("LI")
    li.innerHTML = "<span class='chat-img pull-right'><img class = 'img usr' src='static/img/user_1.jpg' alt='User Avatar'></span><div class='chat-body clearfix'><div class='header'><strong class='primary-font'>John Doe</strong><small class='pull-right text-muted'><i class='fa fa-clock-o'></i> 12 mins ago</small></div><div id='map_canvas' style = 'width:inherit;height:300px;'></div></div>"
    li.className = "right clearfix";
    ulElement.appendChild(li);
    li.scrollIntoView()
    if(position == undefined) {
      var myLatLng = new google.maps.LatLng(30.595227, 32.268501);
    }
    else {
      var myLatLng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
    }
    var mapOptions = {
      zoom: 17,
      center: myLatLng,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    map = new google.maps.Map(document.getElementById('map_canvas'),
                                  mapOptions);
      $.get("http://localhost:5000/valid", function(data){
          for(var i in data["buttons"]){
            addButton(data["buttons"][i])
          }
      });




    map.addListener('click', function(e) {
        placeMarker(e.latLng, map);
    });

    function placeMarker(position, map) {
      if(!ismarked){
          marker = new google.maps.Marker({
          position: position,
          map: map
        });
        map.panTo(position);
        ismarked = true;
      }
    }
}
 		   
function delete_marker(){
  if(ismarked){
      ismarked=false; 
      marker.setMap(null);
  }
}

function fail(){
    var a;
     alert('navigator.geolocation failed, may not be supported');
     initialize(a);
}


