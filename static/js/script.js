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
