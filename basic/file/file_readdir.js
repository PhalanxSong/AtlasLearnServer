var fs = require("fs");

fs.readdir('.', function (err, files) {
    if (err) {
        return console.error(err);
    }
    console.log(files);
});

console.log("程序执行结束!");