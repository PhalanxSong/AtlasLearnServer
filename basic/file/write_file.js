var fs = require("fs");
var data = '上天既赐予我不同於凡人之力，就有我必须去做的事。我若死於此，不但有愧天地，更对不起千千万万崇拜我的苗民黔首！道归道、魔归魔、而我是我，神佛也不能决定我的命运！';

console.log(data);

fs.writeFile('output.txt', data, (error) => {
    if (error) {
        console.log(error);
    } else {
        console.log('成功写入文件');
    }
});

data = '\n            ---赵灵儿';
console.log(data);

fs.appendFile('output.txt', data, (error) => {
    if (error) {
        console.log(error);
    } else {
        console.log('成功写入文件');
    }
});