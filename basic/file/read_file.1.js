var fs = require("fs");

console.log('\n');

fs.readFile('haha.txt', 'utf8', function (err, data) {
    if (err) {
        return console.error(err);
    }
    //console.log(data);

    var data = data.replace(new RegExp('\r'), '');
    var data = data.replace(new RegExp('\n'), '');
    var data = data.replace(new RegExp('\t'), '');
    var data = data.replace(new RegExp(' '), '');

    array = data.split(',');
    for (var i in array) {
        console.log(array[i]);
    }
});

console.log("程序执行结束!");