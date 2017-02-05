var express = require('express');
var router = express.Router();
var path = require('path');
var fs = require("fs");

/* GET home page. */
router.get('/', function (req, res, next) {
	var io = req.io;
	var watchedClass = path.join(__dirname, path.join('..', path.join('public', path.join('watching', 'class.txt'))));
	fs.readFile(watchedClass, 'utf8', function (err, data) {
		if (!err)
			res.render('index', { title: 'ClassiPi Monitor', classification: data });
		else
			console.log("error" + err.message);
	});
});

module.exports = router;
