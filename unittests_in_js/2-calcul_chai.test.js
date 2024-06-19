const calculateNumber = require("./2-calcul_chai");
const chai = require('chai');
const expect = chai.expect;

describe("calculateNumber", function() {
  describe('SUM', () => {
    it("Testing the add function with normal params", function() {
      expect(calculateNumber('SUM', 1, 2)).to.equal(3);
    });
    it("Testing add with one float number", function() {
      expect(calculateNumber('SUM', 30, 15.3)).to.equal(45);
    });
    it("Testing add with two float numbers", function() {
      expect(calculateNumber('SUM', 11.1, 77.7)).to.equal(89);
    });
    it("Testing add with floats that end with .5", function() {
      expect(calculateNumber('SUM', 3.5, 9.5)).to.equal(14);
    });
    it("works with negative number and positive", function() {
      expect(calculateNumber('SUM', 100, -50)).to.equal(50);
    });
    it("works with two negative numbers", function() {
      expect(calculateNumber('SUM', -1, -9)).to.equal(-10);
    });
  });

  describe('SUBTRACT', () => {
    it("works properly with SUBTRACT, normal params", function() {
      expect(calculateNumber('SUBTRACT', 3, 2)).to.equal(1);
    });
    it("works properly with SUBTRACT, with first num as float", function() {
      expect(calculateNumber('SUBTRACT', 8.8, 5)).to.equal(4);
    });
    it("works properly with SUBTRACT, with second num as float", function() {
      expect(calculateNumber('SUBTRACT', 8, 5.2)).to.equal(3);
    });
    it("works properly with SUBTRACT, with 2 float params", function() {
      expect(calculateNumber('SUBTRACT', 33.3, 22.2)).to.equal(11);
    });
    it("works with negative number and positive", function() {
      expect(calculateNumber('SUBTRACT', -13, 9)).to.equal(-22);
    });
    it("works with 2 negative numbers", function() {
      expect(calculateNumber('SUBTRACT', -13, -99)).to.equal(86);
    });
  });

  describe('DIVIDE', () => {
    it("works properly with DIVIDE, normal params", function() {
      expect(calculateNumber('DIVIDE', 10, 5)).to.equal(2);
    });
    it("works properly with DIVIDE, rounding first num", function() {
      expect(calculateNumber('DIVIDE', 200.3, 5)).to.equal(40);
    });
    it("works properly with DIVIDE, rounding second num", function() {
      expect(calculateNumber('DIVIDE', 200, 5.1)).to.equal(40);
    });
    it("checks if negatives works properly with DIVIDE", function() {
      expect(calculateNumber('DIVIDE', -10, 5)).to.equal(-2);
    });
    it("checks if floats works properly with DIVIDE", function() {
      expect(calculateNumber('DIVIDE', 53.3, 1.8)).to.equal(26.5);
    });
    it("checks if Error was raised when divided by zero", function() {
      expect(calculateNumber('DIVIDE', 15, 0).toLowerCase()).to.equal('error');
    });
  });
});
