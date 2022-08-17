
  const  createPushNotificationsJobs= (jobs,queue)=> {
     if (!Array.isArray(jobs)) {
         throw new Error('jobs must be an array');
     }

     for (const job of jobs) {
        let job1= queue.create('push_notification_code_3', job);

        job1.on('enqueue', () => {
            console.log('Notification job created:', job1.id);
        })
        .on('complete', () => {
            console.log(`Notification job ${job1.id} completed`);
        })
        .on('failed', (err) => {
            console.log(`Notification job ${job1.id} failed: ${err}`);
        })
        .on('progress', (progress, total) => {
            console.log('Notification job', job1.id, `${progress}% complete`);
        })
        .save();


     }

 }
  module.exports = createPushNotificationsJobs;