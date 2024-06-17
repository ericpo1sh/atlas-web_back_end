// Reading a file asynchronously with Node JS 
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load from the database'));
      }
      const lines = data.split('\n').filter(line => line.trim() !== '');

      const students = lines.slice(1);
      const studentCount = students.length;
      console.log(`Number of students: ${studentCount}`);

      const fields = []
      students.forEach((student) => {
        const details = student.split(',');
        const firstName = details[0].trim();
        const field = details[3].trim();

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      });

      for (const [field, names] of Object.entries(fields)) {
        console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }
      resolve(studentCount);
    });
  });
}

module.exports = countStudents
