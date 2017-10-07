const express = require('express');

const mongoose = require('mongoose');

// 保护 NodeJS 应用安全
const helmet = require('helmet');

// http 请求体解析
const bodyParser = require('body-parser');

// express 默认日志组件
const morgan = require('morgan');

// mongoose 推荐 promise 化
const bluebird = require('bluebird');

const config = require('./config');

const routes = require('./routes');

const auth = require('basic-auth-connect');

const app = express();

app.use(morgan('combined'));

if (config.needAuth) {
  console.log('this server need auth ...');
  app.use(auth(config.mongo.adminUsername, config.mongo.adminPassword));
}

mongoose.Promise = bluebird;
mongoose.connect(config.mongo.url);


// ??????????? 似乎是允许本目录下的 public 文件夹 文件访问?
app.use(function (req, res, next) {
  // allow a-frame to get assets.
  var matchUrl = '/public';
  if (req.url.substring(0, matchUrl.length) === matchUrl) {
    res.setHeader("Access-Control-Allow-Origin", "*");
  }
  return next();
});


app.use(helmet());
app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(bodyParser.json());
app.use('/', routes);
app.use(require('./middlewares/error-handler'));
app.use('/public/assets', express.static(__dirname + '/uploads/assets'));

app.listen(config.server.port, () => {
  console.log('Magic about asset happens on port : ' + config.server.port + ' ...');
});

module.exports = app;