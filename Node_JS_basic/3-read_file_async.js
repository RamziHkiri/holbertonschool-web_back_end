const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
      } else {
        const contents = data.trim().split('\n');
        const students = contents.map((content) => content.split(','));
        const fields = {};
        console.log((`Number of students: ${students.length - 1}`));

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
            console.log(`Number of students in ${f[field]}: ${fields[f[field]].list.length}. List: ${fields[f[field]].list.join(', ')}`);
          }
        }

        resolve();
      }
    });
  });
}

module.exports = countStudents;
