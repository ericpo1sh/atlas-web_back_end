// 6. Async tests with done 
function getPaymentTokenFromAPI(success) {
  if (success === true) {
    resolve({data: 'Successful response from the API'});
  }
}
module.exports = getPaymentTokenFromAPI;
