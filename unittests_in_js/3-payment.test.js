const sendPaymentRequestToApi = require("./3-payment");
const Utils = require("./utils");
const sinon = require('sinon');
const chai = require('chai');
const expect = chai.expect;

describe('sendPaymentRequestToAPI', function() {
  let spy = sinon.spy(Utils, 'sendPaymentRequestToApi');
  it('makes sure the math is the same used as the utils method', function () {
    sendPaymentRequestToApi(99, 30);
    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('SUM', 99, 30)).to.be.true;
  });
});
