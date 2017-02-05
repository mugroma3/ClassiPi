var socket = io();
socket.on('newImage', function (msg) {
	document.getElementById("image").src = "watching/image.jpg?" + new Date().getTime();
});
socket.on('newClass', function (msg) {
	document.getElementById("classification").innerHTML = msg;
});