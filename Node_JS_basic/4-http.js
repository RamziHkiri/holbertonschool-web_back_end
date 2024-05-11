const http = require('http');

const server = http.createServer((req, res) => {
  res.end('Hello Holberton School!');
});

const app = server.listen(1245, () => {
  console.log(' run Server on port 1245');
});

module.exports = app;
