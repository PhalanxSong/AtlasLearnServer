const Model = require('../../lib/facade');
const assetRecordSchema = require('./asset-record-schema');

class AssetRecordModel extends Model {
	findOneAndUpdate(conditions, update) {
		return this.Schema
			.findOneAndUpdate(conditions, update, {
				new: true,
				upsert: true
			})
			.exec();
	}

	findAllOfRecord(recordId) {
		return this.Schema
			.find({
				recordId
			})
			.populate('assetId')
			.exec();
	}
}

module.exports = new AssetRecordModel(assetRecordSchema);