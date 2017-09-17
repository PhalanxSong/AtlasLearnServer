const Event = require('../models/event');

let id = '59ba4c26967c962aeb74fa95';
let body = {
    title: 'GDC 2666'
}

// { new: true } then 返回的值为 更新后的值
// { new: false } then 返回的值为 更新前的值
Event
    .findByIdAndUpdate(id, { $set: body }, { new: true })
    .then(document => console.log('\n更新文档:\n', document));
