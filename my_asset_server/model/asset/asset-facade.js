const Model = require('../../lib/facade');
const assetSchema = require('./asset-schema');

class AssetModel extends Model {}

module.exports = new AssetModel(assetSchema);