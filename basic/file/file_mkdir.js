var fs = require("fs");

fs.mkdir('logs', (error) => {
    if (error) {
        console.log(error);
    } else {
        console.log('成功创建目录: logs');

        fs.writeFile('logs/temp1', 'temp1', (error) => {
            if (error) {
                console.log(error);
            } else {
                console.log('成功写入文件');
            }
        });

        fs.writeFile('logs/temp2', 'temp2', (error) => {
            if (error) {
                console.log(error);
            } else {
                console.log('成功写入文件');
            }
        });
    }
});
