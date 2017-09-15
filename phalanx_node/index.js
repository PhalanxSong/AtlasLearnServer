console.log('hello...this is index.js');

const os = require('os');
console.log('os host name : ' + os.hostname());

const request = require('request');
request({
    url: 'https://api.douban.com/v2/movie/top250',
    json: true
}, (error, response, body) => {
    console.log(JSON.stringify(body, null, 2))
});

const greeting = require('./greeting');
greeting.sayHello('Phalanx Song');