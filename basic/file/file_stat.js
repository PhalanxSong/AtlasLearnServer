var fs = require("fs");

fs.stat('input.txt', (error, stats) => {
    if (error) {
        console.log(error);
    } else {
        console.log(stats);
        console.log(`bIsFile : ${stats.isFile()}`);
        console.log(`bIsDirectory : ${stats.isDirectory()}`);
    }
})