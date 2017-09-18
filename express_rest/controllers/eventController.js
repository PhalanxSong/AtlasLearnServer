const event = require('../models/event');

const index = (req, res) => {
    event
        .find()
        .then(documents => res.send(documents));
}

const store = (req, res) => {
    console.log(req.body);

    const reqEvent = new event({
        title: req.body.title
    });

    reqEvent
        .save()
        .then(document => res.send(document));
}

const show = (req, res) => {
    const id = req.params.id;
    event.findById(id)
        .then(document => res.send(document));
}

const update = (req, res) => {
    const id = req.params.id;
    const body = {
        title: req.body.title
    }
    event.findByIdAndUpdate(id, {
            $set: body
        }, {
            new: true
        })
        .then(document => res.send(document));
}

const destroy = (req, res) => {
    const id = req.params.id;
    event.findByIdAndRemove(id)
        .then(document => res.send(document));
}

const destroyAll = (req, res) => {
    event.remove().then(document => {
        res.send('delete all events');
    });
}

const createDefault = (req, res) => {
    const data = require('../database/operation/seeds/simple_events.json');
    event.insertMany(data)
        .then(() => res.send('create default events'))
        .catch(error => res.send(error));
}

module.exports = {
    index,
    store,
    show,
    update,
    destroy,
    destroyAll,
    createDefault
}