const calculateNumber = require("./2-calcul_chai");
const expect = require('chai').expect;

describe("calculateNumber", function() {
  describe('SUM', () => {
    it("Testing the add function with normal params", function() {
      expect.strictEqual(calculateNumber('SUM', 100, 200), 300)
    });
    it("Testing add with one float number", function() {
      expect.strictEqual(calculateNumber('SUM', 5, 5.9), 11)
    });
    it("Testing add with two float numbers", function() {
      expect.strictEqual(calculateNumber('SUM', 11.1, 77.7), 89)
    });
    it("Testing add with floats that end with .5", function() {
      expect.strictEqual(calculateNumber('SUM', 3.5, 9.5), 14)
    });
    it("works with negative number and positive", function() {
      expect.strictEqual(calculateNumber('SUM', -1, 9), 8)
    });
    it("works with two negative numbers", function() {
      expect.strictEqual(calculateNumber('SUM', -1, -9), -10)
    });
  })
  describe('SUBTRACT', () => {
    it("works properly with SUBTRACT, normal params", function() {
      expect.strictEqual(calculateNumber('SUBTRACT', 3, 2), 1)
    })
    it("works properly with SUBTRACT, with first num as float", function() {
      expect.strictEqual(calculateNumber('SUBTRACT', 12.6, 5), 8)
    })
    it("works properly with SUBTRACT, with second num as float", function() {
      expect.strictEqual(calculateNumber('SUBTRACT', 12, 5.3), 7)
    })
    it("works properly with SUBTRACT, with 2 float params", function() {
      expect.strictEqual(calculateNumber('SUBTRACT', 233.3, 22.2), 211)
    })
    it("works with negative number and positive", function() {
      expect.strictEqual(calculateNumber('SUBTRACT', 4, -9), 13)
    })
    it("works with 2 negative numbers", function() {
      expect.strictEqual(calculateNumber('SUBTRACT', -4, -9), 5)
    })
  });
  describe('DIVIDE', () => {
    it("works properly with DIVIDE, normal params", function() {
      expect.strictEqual(calculateNumber('DIVIDE', 200, 5), 40)
    })
    it("works properly with DIVIDE, rounding first num", function() {
      expect.strictEqual(calculateNumber('DIVIDE', 200.3, 5), 40)
    })
    it("works properly with DIVIDE, rounding second num", function() {
      expect.strictEqual(calculateNumber('DIVIDE', 200, 5.1), 40)
    })
    it("checks if negatives works properly with DIVIDE", function() {
      expect.strictEqual(calculateNumber('DIVIDE', -20, 10), -2)
    })
    it("checks if floats works properly with DIVIDE", function() {
      expect.strictEqual(calculateNumber('DIVIDE', 53.3, 1.8), 26.5)
    })
    it("checks if Error was raised when divided by zero", function() {
      expect.strictEqual(calculateNumber('DIVIDE', 15, 0).toLowerCase(), 'error')
    })
  });
});
