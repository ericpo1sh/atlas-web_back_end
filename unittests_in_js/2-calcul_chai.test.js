const calculateNumber = require("./2-calcul_chai.js");
const expect = require('chai').expect;

describe("calculateNumber", function() {
  describe('SUM', () => {
    it("Testing the add function with normal params", function() {
      expect.strictEqual(calculateNumber('SUM', 1, 2), 3)
      expect.strictEqual(calculateNumber('SUM', 2, 3), 5)
      expect.strictEqual(calculateNumber('SUM', 100, 200), 300)
    });
    it("Testing add with one float number", function() {
      expect.strictEqual(calculateNumber('SUM', 5, 5.9), 11)
      expect.strictEqual(calculateNumber('SUM', 5.9, 10), 16)
      expect.strictEqual(calculateNumber('SUM', 30, 15.3), 45)
    });
    it("Testing add with two float numbers", function() {
      expect.strictEqual(calculateNumber('SUM', 11.1, 77.7), 89)
      expect.strictEqual(calculateNumber('SUM', 1.1, 4.7), 6)
      expect.strictEqual(calculateNumber('SUM', 3.9, 0.9), 5)
    });
    it("Testing add with floats that end with .5", function() {
      expect.strictEqual(calculateNumber('SUM', 3.5, 9.5), 14)
      expect.strictEqual(calculateNumber('SUM', 12.5, 3.5), 17)
      expect.strictEqual(calculateNumber('SUM', 100.5, 98.5), 200)
    });
    it("works with negative number and positive", function() {
      expect.strictEqual(calculateNumber('SUM', -1, 9), 8)
      expect.strictEqual(calculateNumber('SUM', -4, 9), 5)
      expect.strictEqual(calculateNumber('SUM', 100, -50), 50)
    });
    it("works with two negative numbers", function() {
      expect.strictEqual(calculateNumber('SUM', -1, -9), -10)
      expect.strictEqual(calculateNumber('SUM', -4, -9), -13)
      expect.strictEqual(calculateNumber('SUM', -100, -50), -150)
    });
  })
  describe('SUBTRACT', () => {
    it("works properly with SUBTRACT, normal params", function() {
      expect.strictEqual(calculateNumber('SUBTRACT', 3, 2), 1)
      expect.strictEqual(calculateNumber('SUBTRACT', 13, 12), 1)
      expect.strictEqual(calculateNumber('SUBTRACT', 43, 32), 11)
    })
    it("works properly with SUBTRACT, with first num as float", function() {
      expect.strictEqual(calculateNumber('SUBTRACT', 12.6, 5), 8)
      expect.strictEqual(calculateNumber('SUBTRACT', 1.6, 5), -3)
      expect.strictEqual(calculateNumber('SUBTRACT', 8.8, 5), 4)
    })
    it("works properly with SUBTRACT, with second num as float", function() {
      expect.strictEqual(calculateNumber('SUBTRACT', 12, 5.3), 7)
      expect.strictEqual(calculateNumber('SUBTRACT', 1, 5.1), -4)
      expect.strictEqual(calculateNumber('SUBTRACT', 8, 5.2), 3)
    })
    it("works properly with SUBTRACT, with 2 float params", function() {
      expect.strictEqual(calculateNumber('SUBTRACT', 33.3, 22.2), 11)
      expect.strictEqual(calculateNumber('SUBTRACT', 133.3, 22.2), 111)
      expect.strictEqual(calculateNumber('SUBTRACT', 233.3, 22.2), 211)
    })
    it("works with negative number and positive", function() {
      expect.strictEqual(calculateNumber('SUBTRACT', -13, 9), -22)
      expect.strictEqual(calculateNumber('SUBTRACT', 13, -99), 112)
      expect.strictEqual(calculateNumber('SUBTRACT', 4, -9), 13)
    })
    it("works with 2 negative numbers", function() {
      expect.strictEqual(calculateNumber('SUBTRACT', -13, -9), -4)
      expect.strictEqual(calculateNumber('SUBTRACT', -13, -99), 86)
      expect.strictEqual(calculateNumber('SUBTRACT', -4, -9), 5)
    })
  });
  describe('DIVIDE', () => {
    it("works properly with DIVIDE, normal params", function() {
      expect.strictEqual(calculateNumber('DIVIDE', 10, 5), 2)
      expect.strictEqual(calculateNumber('DIVIDE', 6, 2), 3)
      expect.strictEqual(calculateNumber('DIVIDE', 200, 5), 40)
    })
    it("works properly with DIVIDE, rounding first num", function() {
      expect.strictEqual(calculateNumber('DIVIDE', 10.1, 5), 2)
      expect.strictEqual(calculateNumber('DIVIDE', 6.2, 2), 3)
      expect.strictEqual(calculateNumber('DIVIDE', 200.3, 5), 40)
    })
    it("works properly with DIVIDE, rounding second num", function() {
      expect.strictEqual(calculateNumber('DIVIDE', 10, 5.3), 2)
      expect.strictEqual(calculateNumber('DIVIDE', 6, 2.4), 3)
      expect.strictEqual(calculateNumber('DIVIDE', 200, 5.1), 40)
    })
    it("checks if negatives works properly with DIVIDE", function() {
      expect.strictEqual(calculateNumber('DIVIDE', -10, 5), -2)
      expect.strictEqual(calculateNumber('DIVIDE', -15, 3), -5)
      expect.strictEqual(calculateNumber('DIVIDE', -20, 10), -2)
    })
    it("checks if floats works properly with DIVIDE", function() {
      expect.strictEqual(calculateNumber('DIVIDE', 33.3, 22.2), 1.5)
      expect.strictEqual(calculateNumber('DIVIDE', 23.3, 5.2), 4.6)
      expect.strictEqual(calculateNumber('DIVIDE', 53.3, 1.8), 26.5)
    })
    it("checks if Error was raised when divided by zero", function() {
      expect.strictEqual(calculateNumber('DIVIDE', 15, 0).toLowerCase(), 'error')
      expect.strictEqual(calculateNumber('DIVIDE', 1, 0).toLowerCase(), 'error')
      expect.strictEqual(calculateNumber('DIVIDE', 3, 0).toLowerCase(), 'error')
    })
  });
});
