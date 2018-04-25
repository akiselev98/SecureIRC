function makeid() {
  var text = "";
  var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

  for (var i = 0; i < 20; i++)
    text += possible.charAt(Math.floor(Math.random() * possible.length));

  return text;
}

function update_userlist() {
    
}

var username = "{{ current_user.username }}";
var socket;
var myStorage = window.localStorage;
var key;
var userlist;
$(document).ready(function(){
    socket = io.connect('https://' + document.domain + ':' + location.port + '/chat');
    socket.on('connect', function() {
	$('#chat').val('');
	//username = prompt("Please enter a username.","");
	//if (username != null && username != "") {
	
	myStorage.setItem('username', username);
	var PassPhrase = makeid();
	myStorage.setItem('seed', PassPhrase);
	var Bits = 1024;
	key = cryptico.generateRSAKey(PassPhrase, Bits);
	var publicKey = cryptico.publicKeyString(key);
	var keyid = cryptico.publicKeyID(publicKey);
        socket.emit('joined', {"username": username, "key": publicKey, "id": keyid});
    //}

    });
    socket.on('status', function(data) {
        $('#chat').val($('#chat').val() + '<' + data.msg + '>\n');
        $('#chat').scrollTop($('#chat')[0].scrollHeight);
    });
    socket.on('message', function(data) {
	console.log(data.msg);
	var messages = JSON.parse(data.msg);
	var encryptedMsg = messages[username];
	var msg = cryptico.decrypt(encryptedMsg, key).plaintext;
        $('#chat').val($('#chat').val() + msg + '\n');
        $('#chat').scrollTop($('#chat')[0].scrollHeight);
    });
    socket.on('userlist_update', function(data) {
	//console.log(data.toString());
	userlist = data;
	$.ajax({
	    url: "/{{ roomname }}/userlist",
	    type: "get",
	    //data: {jsdata: ""}, //TODO: send room ID
	    success: function(response) {
		$("#user-list").html(response);
	    }
	});
    });
    $('#text').keypress(function(e) {
        var code = e.keyCode || e.which;
        if (code == 13) {
            text = username + ": " + $('#text').val();
            $('#text').val('');
	    //var key = JSON.parse(myStorage.getItem('key'));
	    var Bits = 1024;
	    var PassPhrase = myStorage.getItem
	    var publicKey = cryptico.publicKeyString(key);
	    var messageManifest = {};
	    for(var user in userlist){
		var EncryptionResult = cryptico.encrypt(text, userlist[user]);
		messageManifest[user] = EncryptionResult.cipher.toString();
	    }
	    //var EncryptionResult = cryptico.encrypt(text, publicKey);
	    //console.log(EncryptionResult.cipher);
	    //var encryptedText = EncryptionResult.cipher.toString();
	    var encryptedText = JSON.stringify(messageManifest);
            socket.emit('text', {msg: encryptedText});
        }
    });
});

