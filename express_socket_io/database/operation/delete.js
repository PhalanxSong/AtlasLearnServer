const Event = require('../../models/event');

let id = '59ba4c26967c962aeb74fa91';

Event
    .findByIdAndRemove(id)
    .then(document => console.log('\n删除文档:\n', document));
