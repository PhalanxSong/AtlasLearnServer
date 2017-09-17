const Event = require('../../models/event');

let id = '59ba4c26967c962aeb74fa95';
let body = {
    title: 'GDC 2666'
}

Event
    .findByIdAndUpdate(id, { $set: body }, { new: true })
    .then(document => console.log('\n更新文档:\n', document));
