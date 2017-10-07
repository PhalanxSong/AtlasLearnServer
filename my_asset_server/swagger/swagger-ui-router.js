const swaggerUI = require('swagger-tools/middleware/swagger-ui');
const swaggerObject = require('./swagger.json');

module.exports = swaggerUI(swaggerObject);