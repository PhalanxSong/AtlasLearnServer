var fs = require("fs");

fs.readFile('input.txt', function (err, data) {
    if (err) {
        return console.error(err);
    }
    //没有 toString 会输出二进制
    console.log(data.toString());
});

console.log('\n');

fs.readFile('input.txt', 'utf8', function (err, data) {
    if (err) {
        return console.error(err);
    }
    console.log(data);
});

console.log("程序执行结束!");