const event = require('../models/event')

const index = (req, res) => {
    event
        .find()
        .then(documents => res.send(documents));
}

module.exports = {
    index
}