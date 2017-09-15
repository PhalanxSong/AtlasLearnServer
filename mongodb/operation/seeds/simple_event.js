const data = require('./simple_events.json');
const Event = require('../../models/event.js');

Event
    .insertMany(data)
    .then(() => console.log('save data json array success!'))
    .catch(error => console.log(error));