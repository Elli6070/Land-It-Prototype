var net = require('net');
var express = require("express");
var io = require("socket.io-client");
var pythonPath = '/home/pi/landIt/main copy.py';

// Use python shell to call dispensation
let {PythonShell} = require('python-shell')

var host='line-us.local';

// Line-Us socket
var client = new net.Socket();

// Web app socket
var socket = io.connect("http://land-it-prototype.com:3000");

// Commands to write to printer
var commands = [
'G01 X900 Y300 Z0',
    'G01 X900 Y-300 Z0',
    'G01 X900 Y-300 Z1000'];

// Connect to Line-Us
setTimeout(function() {
client.connect(1337, host, function() {
    console.log('Connected to line-us');
    cmdIndex=-1;
});
}, 7000);

socket.on("print message", (msg) => {
	client.on('data', function(data) {
		//sleep(2000);
		console.log('Received: ' + data);
		
		// last command (or connecting) was successfull, so let's send a new command
		if(data.indexOf("hello")==0 || data.indexOf("ok ")==0)
		{
			cmdIndex++;
			console.log('Sending: '+commands[cmdIndex]);
			client.write(commands[cmdIndex]+'\x00\n');
		}
		
		if(data.indexOf('error')==0)
		{
			console.log('Error in command '+cmdIndex);
			console.log('Disconnecting...');
			client.destroy();
		}

		// reached end of command array
		if(cmdIndex==commands.length)
		{
			console.log('Finished!');
			client.destroy();
		}
	});
});

client.on('close', function() {
	console.log('Connection closed');
	console.log('Beginning Dispensation');
	PythonShell.run('/home/pi/landIt/main copy.py', null, function (err, results) {
		console.log('Dispensation Finished');
	});
});

