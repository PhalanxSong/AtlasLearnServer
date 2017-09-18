const mongoose = require('mongoose');

const uri = 'mongodb://localhost:27017/phalanxdb';
const options = {
    useMongoClient: true
};

mongoose.Promise = global.Promise;
mongoose
    .connect(uri, options)
    .then(db => console.log('connect to mongodb success!'))
    .catch(error => console.log('connect to mongodb failed...'));

module.exports = mongoose;