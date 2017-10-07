const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const uuid = require('uuid');
const shortid = require('shortid');

const assetSchema = new Schema({
	_id: {
		type: String,
		default: uuid.v1
	},
	_shortid: {
		type: String,
		default: shortid.generate
	},
	assetUrl: {
		type: String,
		required: true
	},
	creatorId: {
		type: String,
		required: true
	},
	name: {
		type: String
	}
}, {
	timestamps: true
});

module.exports = mongoose.model('Asset', assetSchema);