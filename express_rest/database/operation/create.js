const Event = require('../../models/event');

const event_1 = new Event({
    title: 'NodeJs 开发者大会'
});

event_1
    .save()
    .then(document => console.log(document))
    .catch(error => console.log(error));