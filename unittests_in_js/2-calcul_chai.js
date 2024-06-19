// calculateNumber function that takes two ints
// and a type and returns based on type of equation
function calculateNumber(type, a, b) {
  if (type == 'SUM') {
    return Math.round(a) + Math.round(b);
  }
  if (type == 'SUBTRACT') {
    return Math.round(a) - Math.round(b);
  }
  if (type == 'DIVIDE') {
    if (b == 0) {
      return 'Error';
    }
    return Math.round(a) / Math.round(b);
  }
}
module.exports = calculateNumber;
