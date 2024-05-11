const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8').split('\n');
    while (data[data.length - 1] === '') {
      data.pop();
    }
    const students = data.map((line) => line.split(','));
    console.log((`Number of students: ${students.length - 1}`));
    const fields = {};
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
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;
