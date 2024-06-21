// testing for payment_token function
const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function() {
  it('should return a resolved promise object if true', function(done) {
    getPaymentTokenFromAPI(true);
  })
})
