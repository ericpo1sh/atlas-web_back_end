const kue = require('kue');

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    return Error('Jobs is not an array');
  }
  jobs.forEach((job_data) => {
    const newJob = queue.create('push_notification_code_3', job_data).save((err) => {
      if (!err) {
        console.log('Notification job created: ' + newJob.id);
      }
    })
    newJob.on('complete', () => {
      console.log(`Notification job ${newJob.id} completed`);
    })
    newJob.on('failed', (err) => {
      console.log(`Notification job JOB_ID failed: ${err}`)
    })
    newJob.on('progress', (progress) => {
      console.log(`Notification job ${newJob.id} ${progress}% complete`)
    })
  })
}
module.exports = createPushNotificationsJobs
