var fs = require('fs');
var csv = require('csv');

function VerifyCsv(data) {
    var supportedLanguage = [];
    var topLine = data[0];
    for (var i in topLine) {
        if (i != 0) {
            if (topLine[i] in supportedLanguage) {
                console.log('language id strange : ' + topLine[i]);
                return false;
            } else {
                supportedLanguage.push(topLine[i]);
            }
        }
    }

    var languageCount = supportedLanguage.length;

    var errorCountLine = [];
    for (var i in data) {
        if (i != 0) {
            var localizationTextSet = data[i];
            if (data[i].length != languageCount + 1) {
                errorCountLine.push(localizationTextSet);
            }
        }
    }
    if (errorCountLine.length != 0) {
        console.log('strange count localization text set : ');
        console.log(errorCountLine);
        return false;
    }

    var localizationTextIdArray = [];
    var errorIdArray = [];
    for (var i in data) {
        if (i != 0) {
            var localizationTextSet = data[i];
            if (localizationTextSet[0] in localizationTextIdArray) {
                errorIdArray.push(localizationTextSet[0]);
            } else {
                localizationTextIdArray.push(localizationTextSet[0]);
            }
        }
    }
    if (errorIdArray.length != 0) {
        console.log('error id : ');
        console.log(errorIdArray);
        return false;
    }

    return true;
}

function ConvertCsv(data) {

    fs.exists('./localization_text_file', (exist) => {
        if (!exist) {
            fs.mkdirSync('./localization_text_file');
        }

        var languageJsonArray = {};
        for (var i in data[0]) {
            if (i != 0) {
                languageJsonArray[i.toString()] = {}
                languageJsonArray[i.toString()].name = data[0][i];
                languageJsonArray[i.toString()].json = {};
            }
        }

        for (var i in data) {
            if (i != 0) {
                var localizationTextSet = data[i];
                var id = localizationTextSet[0];
                for (var j in localizationTextSet) {
                    if (j != 0) {
                        languageJsonArray[j.toString()].json[id] = localizationTextSet[j];
                    }
                }
            }
        }

        var allLanguageFile = {};

        for (var i in languageJsonArray) {
            var name = languageJsonArray[i.toString()].name;
            var json = languageJsonArray[i.toString()].json;
            var filePath = './localization_text_file/' + name + '.json';
            allLanguageFile[name] = json;
            console.log('开始写入文件 : ' + filePath);
            fs.writeFile(filePath, JSON.stringify(json), (error) => {
                if (error) {
                    console.log(error);
                } else {
                    console.log('成功写入文件');
                }
            });
        }

        var allLanguageFilePath = './localization_text_file/full.json';
        console.log('开始写入文件 : ' + allLanguageFilePath);
        fs.writeFile(allLanguageFilePath, JSON.stringify(allLanguageFile), (error) => {
            if (error) {
                console.log(error);
            } else {
                console.log('成功写入文件');
            }
        });
    });
}

fs.readFile('./localization-utf8.csv', 'utf8', function (err, data) {
    if (err) {
        return console.error(err);
    } else {
        csv.parse(data, {
            comment: '#'
        }, function (err, output) {
            if (err) {
                return console.error(err);
            } else {

                if (VerifyCsv(output)) {
                    ConvertCsv(output);
                }
            }
        });
    }
});