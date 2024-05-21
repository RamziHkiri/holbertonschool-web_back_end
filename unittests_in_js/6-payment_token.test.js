const { expect } = require('chai');
const chai = require('chai');
const chaiAsPromised = require('chai-as-promised');
const getPaymentTokenFromAPI = require('./6-payment_token');

chai.use(chaiAsPromised);

describe('getPaymentTokenFromAPI', function () {
  it('should return a resolved promise with the correct object when success is true', function () {
    return expect(getPaymentTokenFromAPI(true)).to.eventually.deep.equal({ data: 'Successful response from the API' });
  });

  it('should do nothing when success is false', function () {
    return expect(getPaymentTokenFromAPI(false)).to.be.undefined;
  });
});
