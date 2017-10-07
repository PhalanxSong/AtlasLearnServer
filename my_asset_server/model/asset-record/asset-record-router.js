const controller = require('./asset-record-controller');
const Router = require('express').Router;
const router = new Router();

const tokenVerify = require('../../middlewares/token-verify');

router.route('/')
	.get((...args) => controller.find(...args))
	.post((...args) => controller.updateOrCreate(...args));

router.route('/of/:recordId')
	.get((...args) => controller.findAllOfRecord(...args));

module.exports = router;