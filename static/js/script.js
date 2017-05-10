function newMessageFromUser(textMessage){
  var ulElement = document.getElementById("chatList");
  var li =document.createElement("LI")
  li.innerHTML = "<span class='chat-img pull-left'><img src='static/img/user_3.jpg' alt='User Avatar'></span><div class='chat-body clearfix'><div class='header'><strong class='primary-font'>John Doe</strong><small class='pull-right text-muted'><i class='fa fa-clock-o'></i> 12 mins ago</small></div><p>"+textMessage+"</p></div>"
  li.className = "left clearfix";
  ulElement.appendChild(li);
}

function newMessageFromChat(textMessage){
  var ulElement = document.getElementById("chatList");
  var li =document.createElement("LI")
  li.innerHTML = "<span class='chat-img pull-right'><img src='static/img/user_1.jpg' alt='User Avatar'></span><div class='chat-body clearfix'><div class='header'><strong class='primary-font'>John Doe</strong><small class='pull-right text-muted'><i class='fa fa-clock-o'></i> 12 mins ago</small></div><p>"+textMessage+"</p></div>"
  li.className = "right clearfix";
  ulElement.appendChild(li);
}
function send() {
  input = document.getElementById("textMessage");
  var message = input.value;
  input.value = "";
  newMessageFromUser(message)
}
$(document).ready(function(){
    $("button").click(function(){
        $.get("http://localhost:5000/allrestaurants", function(data){
            alert("Data: " + data);
        });
    });
});
function addButton(str){
  var x = document.getElementsByTagName("UL");
  button = document.createElement("button");
  button.innerHTML = str;
  //button.setAttribute("class","tag")
  x[0].appendChild(button);
}
