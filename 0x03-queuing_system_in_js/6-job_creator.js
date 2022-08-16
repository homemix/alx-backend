let kue = require('kue');

let queue = kue.createQueue();

let msg = {
    phoneNumber: 123,
    message: 'Hello'
}
let job = queue.create('push_notification_code', msg)
    .save(function (err,) {
        if (!err) console.log(`Notification job created :${job.id}`);
        if (err) console.log(`Notification job failed`);
    }).on('complete', function (job) {
        console.log(`Notification job completed :${job.id}`);
    });
