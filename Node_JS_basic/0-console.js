const fs = require('fs');

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
      fs.readFile(filePath, 'utf8', (err, data) => {
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
          console.log(fields);
          resolve(fields);
        }
      });
    });
}
module.exports = readDatabase;
