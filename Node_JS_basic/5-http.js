const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    let database = process.argv[2];
    if (!database) {
      database = './database.csv';
    }
    fs.readFile(database, 'utf8', (err, data) => {
      if (err) {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('Internal Server Error');
      } else {
        const contents = data.trim().split('\n');
        const students = contents.map((content) => content.split(','));
        const fields = {};
        res.write(('This is the list of our students\n'));
        res.write((`Number of students: ${students.length - 1}`));

        students.forEach((student) => {
          const [firstname, , , field] = student;
          if (!fields[field]) {
            fields[field] = {
              count: 0,
              list: [],
            };
          }
          fields[field].count += 1;
          fields[field].list.push(firstname);
        });
        const f = [];
        for (const field in fields) {
          if (Object.prototype.hasOwnProperty.call(fields, field)) {
            f.push(field);
          }
        }
        f.shift();
        for (const field in f) {
          if (Object.prototype.hasOwnProperty.call(f, field)) {
            res.write(`\nNumber of students in ${f[field]}: ${fields[f[field]].list.length}. List: ${fields[f[field]].list.join(', ')}`);
          }
        }
        res.end();
      }
    });
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

const app = server.listen(1245, () => {
  console.log(' run Server on port 1245');
});

module.exports = app;
