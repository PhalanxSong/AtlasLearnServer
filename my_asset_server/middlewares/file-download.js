const fs = require('fs');
const path = require('path');

module.exports = (basePath) => {
	return (req, res, next) => {
		const filePath = path.join(basePath, req.params.fileUrl);
		fs.access(filePath, fs.constants.R_OK, err => {
			if (err) {
				return res.status(404).json({
					message: 'can not access file'
				});
			}
			const ext = path.extname(req.params.fileUrl);
			const finename = req.params.id + ext;
			return res.download(filePath, finename);
		});
	}
}