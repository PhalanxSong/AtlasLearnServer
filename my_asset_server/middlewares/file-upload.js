const multer = require('multer');
const shortid = require('shortid');
const path = require('path');

module.exports = (dest, fileFieldName) => {
	const storage = multer.diskStorage({
		destination: dest,

		filename(req, file, cb) {
			const tmp = (file.originalname).split('.');
			const format = tmp[tmp.length - 1];
			cb(null, `${shortid.generate()}.${format}`);
		}
	});

	return multer({
		storage: storage
	}).single(fileFieldName);
};