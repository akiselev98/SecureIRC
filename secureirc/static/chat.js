function makeid() {
  var text = "";
  var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

  for (var i = 0; i < 20; i++)
    text += possible.charAt(Math.floor(Math.random() * possible.length));

  return text;
}

function update_userlist() {
    
}

var socket;
var myStorage = window.localStorage;
var key;
$(document).ready(function(){
    socket = io.connect('http://' + document.domain + ':' + location.port + '/chat');
    socket.on('connect', function() {
	$('#chat').val('');
	var username = prompt("Please enter a username.","");
	if (username != null && username != "") {
	    myStorage.setItem('username', username);
	    var PassPhrase = makeid();
	    myStorage.setItem('seed', PassPhrase);
	    var Bits = 1024;
	    key = cryptico.generateRSAKey(PassPhrase, Bits);
	    var publicKey = cryptico.publicKeyString(key);
            socket.emit('joined', {"username": username, "key": publicKey, "id": cryptico.publicKeyID(publicKey)});
	}

    });
    socket.on('status', function(data) {
        $('#chat').val($('#chat').val() + '<' + data.msg + '>\n');
        $('#chat').scrollTop($('#chat')[0].scrollHeight);
    });
    socket.on('message', function(data) {
        $('#chat').val($('#chat').val() + data.msg + '\n');
        $('#chat').scrollTop($('#chat')[0].scrollHeight);
    });
    $('#text').keypress(function(e) {
        var code = e.keyCode || e.which;
        if (code == 13) {
            text = $('#text').val();
            $('#text').val('');
	    //var key = JSON.parse(myStorage.getItem('key'));
	    var Bits = 1024;
	    var PassPhrase = myStorage.getItem
	    var publicKey = cryptico.publicKeyString(key);
	    
	    var EncryptionResult = cryptico.encrypt(text, publicKey);
	    console.log(EncryptionResult.cipher);
	    var encryptedText = EncryptionResult.cipher.toString();
            socket.emit('text', {msg: text});
        }
    });
});

