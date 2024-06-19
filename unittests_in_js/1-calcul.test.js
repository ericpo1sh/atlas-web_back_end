const calculateNumber = require("./1-calcul");
var assert = require('assert')

describe("Testing 1-calcul function", function() {
// testing addition
  it("Testing the add function with params 1, 2", function() {
    assert.strictEqual(calculateNumber('SUM', 1, 2), 3)
  });
  it("Testing add with one float number, 5, 5.9", function() {
    assert.strictEqual(calculateNumber('SUM', 5, 5.9), 11)
  });
  it("Testing add with two float numbers, 11.1, 77.7", function() {
    assert.strictEqual(calculateNumber('SUM', 11.1, 77.7), 89)
  });
  it("Testing add with 3.5, 9.5", function() {
    assert.strictEqual(calculateNumber('SUM', 3.5, 9.5), 14)
  });
  it("works with negative number and positive, -1, 9", function() {
    assert.strictEqual(calculateNumber('SUM', -1, 9), 8)
  });
// testing subtract 
  it("works properly with SUBTRACT, params: 3, 2", function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 3, 2), 1)
  })
  it("works properly with SUBTRACT, with float params: 12.6, 5", function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 12.6, 5), 8)
  })
  it("works properly with SUBTRACT, with 2 float params: 33.3, 22.2", function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 33.3, 22.2), 11)
  })
  it("works with negative number and positive, -13, 9", function() {
    assert.strictEqual(calculateNumber('SUBTRACT', -13, 9), -22)
  })
// testing divide
  it("works properly with DIVIDE, params: 10, 5", function() {
    assert.strictEqual(calculateNumber('DIVIDE', 10, 5), 2)
  })
  it("checks if negatives works properly with DIVIDE, params: -10, 5", function() {
    assert.strictEqual(calculateNumber('DIVIDE', -10, 5), -2)
  })
  it("checks if floats works properly with DIVIDE, params: 33.3, 22.2", function() {
    assert.strictEqual(calculateNumber('DIVIDE', 33.3, 22.2), 1.5)
  })
  it("checks if Error was raised when divided by zero", function() {
    assert.strictEqual(calculateNumber('DIVIDE', 15, 0), 'Error')
  })
});
