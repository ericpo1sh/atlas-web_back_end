const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function () {
    var spy = sinon.spy(Utils, 'calculateNumber');;
    it('makes sure the math is the same used as the utils method', function () {
        sendPaymentRequestToApi(20, 5);
        expect(spy.calledOnceWithExactly('SUM', 20, 5)).to.be.true;
    });
});
