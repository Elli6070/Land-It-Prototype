'use strict';

var fs = require("fs");
var path = require("path");
var express = require("express");
var app = express();
var http = require("http").Server(app);
var io = require("socket.io")(http);

let port = process.env.PORT;
if (port == null || port == "") {
   port = 8000;
}
var index_file = path.join(__dirname, "Index.html");


app.get("/", (req, res) => {
    console.log("Getting Index.html at " + index_file);

    fs.readFile(index_file, (err, index) => {
        if (err) { console.log("Error getting Index.html"); }

        else {
			res.sendFile(index_file);
        }
    });

});

io.on('connection', function(socket){
  socket.on('print message', function(msg){
    console.log('sending message: ' + msg + 'to printer');
	io.emit('print message', msg);
  });
});

http.listen(port, () => console.log("App now listening on port " + port));
