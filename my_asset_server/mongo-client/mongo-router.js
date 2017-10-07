const mongoExpress = require('mongo-express/lib/middleware');
const config = require('./config');

module.exports = mongoExpress(config);