const Controller = require('../../lib/controller');
const assetRecordFacade = require('./asset-record-facade');

class AssetRecordController extends Controller {
	updateOrCreate(req, res, next) {
		let data = req.body;

		let message = '';
		if (!data.assetId) {
			message = 'missing asset id.';
		} else if (!data.recordId) {
			message = 'missing record id.';
		} else if (!data.linkCount) {
			message = 'missing link count.';
		}

		if (message != '') {
			return res.status(422).json({
				message: message
			});
		}

		const conditions = {
			assetId: data.assetId,
			recordId: data.recordId
		};

		this.facade.findOneAndUpdate(conditions, {
				linkCount: data.linkCount
			}, {
				upsert: true
			})
			.then(doc => {
				return res.status(200).json(doc);
			})
			.catch(err => next(err));
	}

	findAllOfRecord(req, res, next) {
		this.facade.findAllOfRecord(req.params.recordId)
			.then(doc => res.status(200).json(doc))
			.catch(err => next(err));
	}
}

module.exports = new AssetRecordController(assetRecordFacade);