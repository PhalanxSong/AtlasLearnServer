var fs = require("fs");
var data = '上天既赐予我不同於凡人之力，就有我必须去做的事。我若死於此，不但有愧天地，更对不起千千万万崇拜我的苗民黔首！道归道、魔归魔、而我是我，神佛也不能决定我的命运！';

console.log(data);

// 创建一个可以写入的流，写入到文件 output.txt 中
var writerStream = fs.createWriteStream('output_stream.txt');

// 使用 utf8 编码写入数据
writerStream.write(data, 'UTF8');

// 标记文件末尾
writerStream.end();

// 处理流事件 --> data, end, and error
writerStream.on('finish', function () {
    console.log("写入完成");
});

writerStream.on('error', function (err) {
    console.log(err.stack);
});

console.log("程序执行完毕");