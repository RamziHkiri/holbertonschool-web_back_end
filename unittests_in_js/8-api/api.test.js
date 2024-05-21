const chai = require('chai');
const chaiHttp = require('chai-http');
const app = require('./api'); // Assuming your Express app is exported from api.js

const { expect } = chai;
chai.use(chaiHttp);

describe('Index page', function() {
  it('should return the correct status code', function(done) {
    chai.request(app)
      .get('/')
      .end((err, res) => {
        expect(res).to.have.status(200);
        done();
      });
  });

  it('should return the correct result', function(done) {
    chai.request(app)
      .get('/')
      .end((err, res) => {
        expect(res.text).to.equal('Welcome to the payment system');
        done();
      });
  });

});
