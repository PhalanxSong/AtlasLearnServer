const controller = require('./asset-controller');
const Router = require('express').Router;
const router = new Router();
const {
  assetUploadDest,
  fileFieldName
} = require('./asset-const');
const upload = require('../../middlewares/file-upload')(assetUploadDest, fileFieldName);
const download = require('../../middlewares/file-download')(assetUploadDest);

const tokenVerify = require('../../middlewares/token-verify');

router.route('/')
  .get((...args) => controller.find(...args))
  .post(tokenVerify, upload, (...args) => controller.create(...args));

router.route('/:id')
  // .put(upload, (...args) => controller.update(...args))
  .get((...args) => controller.findById(...args));
// .delete((...args) => controller.remove(...args));

router.route('/file/:id')
  .get((...args) => controller.downloadFile(...args), download);

module.exports = router;