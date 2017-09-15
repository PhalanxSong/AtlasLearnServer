const Event = require('../models/event');

Event
    .find()
    .then(documents => console.log('\nfind 所有文档:\n', documents));

Event
    .find({ title: 'UE4 游戏开发讲座' })
    .then(documents => console.log('\nfind 指定标题文档:\n', documents));

Event
    .findOne({ title: 'UE4 游戏开发讲座' })
    .then(document => console.log('\nfind one 指定标题文档:\n', document));

Event
    .find({ _id: '59ba4c26967c962aeb74fa94' })
    .then(document => console.log('\nfind one 指定_id文档:\n', document));

Event
    .findById({ _id: '59ba4c26967c962aeb74fa94' })
    .then(document => console.log('\nfind by id:\n', document));
