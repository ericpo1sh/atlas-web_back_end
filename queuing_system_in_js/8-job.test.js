const createPushNotificationsJobs = require('./8-job')
const kue = require('kue');
const assert = require('assert');
const { expect } = require('chai');
const queue = kue.createQueue();

describe('createPushNotificationsJobs', function() {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('displays a error message if jobs is not an array', function(done) {
    assert.throws(() => createPushNotificationsJobs("hello", queue), new Error('Jobs is not an array'));
    done();
  })

  it('checks if it creates two new jobs to the queue', function(done) {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];
    console.log('hello')
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs[0].data).to.equal(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.equal(jobs[1]);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    done();
  })
})
