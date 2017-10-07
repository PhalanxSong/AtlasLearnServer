const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const uuid = require('uuid');

const assetRecordSchema = new Schema({
	_id: {
		type: String,
		default: uuid.v1
	},
	assetId: {
		type: String,
		require: true,
		ref: 'Asset'
	},
	recordId: {
		type: String,
		require: true
	},
	linkCount: {
		type: Number,
		require: true
	}
}, {
	timestamps: true
});

module.exports = mongoose.model('AssetRecord', assetRecordSchema);