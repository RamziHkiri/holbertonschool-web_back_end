const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('checks the output with valid type SUM', () => {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    assert.strictEqual(calculateNumber('SUM',1, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM',1.2, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM',1.5, 3.7), 6);
    assert.strictEqual(calculateNumber('SUM',3.7, 1), 5);
    assert.strictEqual(calculateNumber('SUM',3.7, 1.2), 5);
  });
  it('checks the output with valid type SUBTRACT', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', -1, 3), -4);
    assert.strictEqual(calculateNumber('SUBTRACT',1, 3.7), -2);
    assert.strictEqual(calculateNumber('SUBTRACT',4.2, 3.7), 1);
    assert.strictEqual(calculateNumber('SUBTRACT',5.3, 3), 2);
  });
  it('checks the output with valid type devide', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 6.4, 1), 6);
    assert.strictEqual(calculateNumber('DIVIDE',9.4, 3.7), 3);
    assert.strictEqual(calculateNumber('DIVIDE',-6.4, 3.7), -2);


  });
});