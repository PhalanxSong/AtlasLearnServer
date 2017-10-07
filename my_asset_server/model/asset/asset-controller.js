const Controller = require('../../lib/controller');
const assetFacade = require('./asset-facade');

class AssetController extends Controller {
	create(req, res, next) {
		let data = req.body;
		const file = req.file;
		data.assetUrl = file.filename;
		data.creatorId = req.user.uuid;

		this.facade.create(data)
			.then(doc => res.status(201).json(doc))
			.catch(err => next(err));
	}

	downloadFile(req, res, next) {
		this.facade.findById(req.params.id)
			.then(doc => {
				if (!doc) {
					return res.status(404).json({
						message: `can not find asset ${req.params.id}`
					});
				}
				req.params.fileUrl = doc.assetUrl;
				next();
			})
			.catch(err => next(err));
	}
}

module.exports = new AssetController(assetFacade);