const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('checks the output with valid type SUM', function () {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    assert.strictEqual(calculateNumber('SUM',1, 3.7), 5);
  });
  it('checks the output with valid type SUBTRACT', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', -1, 3), -4);
    assert.strictEqual(calculateNumber('SUBTRACT',1, 3.7), -2);
    
  });
  it('checks the output with valid type devide', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 6.4, 1), 6);
  });
});