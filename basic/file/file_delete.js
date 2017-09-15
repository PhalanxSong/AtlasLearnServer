var fs = require("fs");

fs.readdirSync('logs').map((file) => {
    fs.unlink(`logs/${file}`, (err) => {
        if (err) {
            console.log(err);
        } else {
            console.log(`成功删除了文件:${file}`);
        }
    })
});

fs.rmdir('logs', function (err) {
    if (err) {
        return console.error(err);
    }
    console.log('成功删除目录');
});

console.log("程序执行结束!");