var fs = require("fs");

console.log(' 1 : ------------------');

fs.readFile('input.txt', function (err, data) {
	if (err) {
		console.log(err.stack);
		return;
	}
	console.log(data.toString());
});

console.log(' 2 : ------------------');

fs.readFile('null.txt', function (err, data) {
	if (err) {
		console.log(err.stack);
		return;
	}
	console.log(data.toString());
});
console.log("程序执行完毕");