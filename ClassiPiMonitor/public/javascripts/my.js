function addBold(text) {
	return text.replace(/^###### /g, "<b>")
			   .replace(/\n###### /g, "\n\n<b>")
			   .replace(/######/g, "</b>");
}

document.getElementById("classification").innerHTML = addBold(document.getElementById("classification").innerHTML);

var srcBuffer;

var socket = io();
socket.on('newImage', function (msg) {
	 srcBuffer = "/watching/image.jpg?" + new Date().getTime();
});
socket.on('newClass', function (msg) {
	document.getElementById("classification").innerHTML = addBold(msg);
	document.getElementById("image").src = srcBuffer;
});

