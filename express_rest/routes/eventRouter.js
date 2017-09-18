const express = require('express');
const router = express.Router();
const eventController = require('../controllers/eventController');

router
    .route('/events')
    .get(eventController.index)
    .post(eventController.store);

router
    .route('/events/all')
    .post(eventController.createDefault)
    .delete(eventController.destroyAll);

router
    .route('/events/:id')
    .get(eventController.show)
    .patch(eventController.update)
    .delete(eventController.destroy);

module.exports = router