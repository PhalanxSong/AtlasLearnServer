const path = require('path');
const Router = require('express').Router;
const router = new Router();

const asset = require('./model/asset/asset-router');
const assetRecord = require('./model/asset-record/asset-record-router');

const mongoClient = require('./mongo-client/mongo-router');
const swaggerUI = require('./swagger/swagger-ui-router');

router.route('/').get((req, res) => {
  res.status(200).json({
    message: 'Welcome to PhalanxSong\'s asset server.'
  });
});

router.use('/asset', asset);
router.use('/asset-record', assetRecord);

router.use('/mongo', mongoClient);

router.use('/swagger', swaggerUI);

module.exports = router;