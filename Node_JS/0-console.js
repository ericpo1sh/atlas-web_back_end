// Executing basic javascript with Node JS 
const process = require('process')

function displayMessage(message) {
  process.stdout.write(message + '\n')
}
module.exports = displayMessage
