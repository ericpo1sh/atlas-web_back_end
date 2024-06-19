const calculateNumber = require("./0-calcul");
var assert = require('assert')

describe("Test suite", function() {
  it("Testing the add function with params 1, 2", function() {
    assert.strictEqual(calculateNumber(1, 2), 3)
  });
  it("Testing add with one float number, 5, 5.9", function() {
    assert.strictEqual(calculateNumber(5, 5.9), 11)
  });
  it("Testing add with two float numbers, 11.1, 77.7", function() {
    assert.strictEqual(calculateNumber(11.1, 77.7), 89)
  });
  it("Testing add with 3.5, 9.5", function() {
    assert.strictEqual(calculateNumber(3.5, 9.5), 14)
  });
});
