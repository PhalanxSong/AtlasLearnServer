const data = require('./simple_events.json');
const event = require('../../../models/event.js');

event
    .insertMany(data)
    .then(() => console.log('save data json array success!'))
    .catch(error => console.log(error));