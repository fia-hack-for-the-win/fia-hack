var SHA256 = require("crypto-js/sha256");
var CryptoJS = require("crypto-js");
var fs = require("fs"),
    path = require("path"),
    util = require("util");
var secretKey = "FIA Alerts";

var content;

fs.readFile(path.join(__dirname,"","hurricane1.xml"), 'utf8',function (err,data) {
	if (err) {
	        console.log(err);
                process.exit(1);
        }
        content = util.format(data);
        //console.log(content);
	
	var hash = CryptoJS.HmacSHA256(content, secretKey);
	var base64 = hash.toString(CryptoJS.enc.Base64);
	//console.log("Base64: " + base64);

	var msg = "{ 'alert':"+content+", 'signature':"+base64+" }";

	console.log("ALERT ---> " + msg);

	// Post to F1 Lambda

});

