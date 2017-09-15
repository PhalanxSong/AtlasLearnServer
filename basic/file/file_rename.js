var fs = require("fs");

fs.rename('output.txt', 'output_renamed.txt', function (err) {
    if (err) {
        return console.error(err);
    }
    console.log('重命名文件成功');
});

console.log("程序执行结束!");