const express = require('express');
const fs = require('fs');

const app = express();
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  let database = process.argv[2];
  if (!database) {
    database = './database.csv';
  }
  fs.readFile(database, 'utf8', (err, data) => {
    if (err) {
      res.status(404).send("Sorry, that route doesn't exist. Have a nice day :)");
    } else {
      const contents = data.trim().split('\n');
      const students = contents.map((content) => content.split(','));
      const fields = {};
      const printed = [];

      printed.push('This is the list of our students');
      printed.push(`Number of students: ${students.length - 1}`);
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
          printed.push(`Number of students in ${f[field]}: ${fields[f[field]].list.length}. List: ${fields[f[field]].list.join(', ')}`);
        }
      }
      res.send(printed.join('\n'));
    }
  });
});
app.listen('1245', () => {
  console.log('app listen at http://localhost:1245');
});

module.exports = app;
