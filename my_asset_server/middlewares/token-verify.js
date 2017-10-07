const jwt = require('jsonwebtoken');
const config = require('../config');

module.exports = (req, res, next) => {
  const token = req.query.jwt_token || req.query.api_key;

  if (!token) {
    return res.status(422).json({
      message: 'Missing token'
    });
  }

  jwt.verify(token, config.jwtSecret, (err, payload) => {
    if (err) {
      return next(err);
    }

    if (!payload || !payload.sub) {
      return res.status(422).json({
        message: 'Invalid token'
      });
    }

    req.user = {
      uuid: payload.sub
    };

    return next();
  })
}