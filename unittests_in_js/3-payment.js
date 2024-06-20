// payment function
Utils = require('./utils.js')
function sendPaymentRequestToApi(totalAmount, totalShipping) {
  console.log('The total is: ' + Utils.calculateNumber('SUM', totalAmount, totalShipping))
}
models.export = sendPaymentRequestToApi
