// Reading a file synchronously with Node JS 
const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter(line => line.trim() !== '');

    if (lines.length === 0) {
      throw new Error('Cannot load the database');
    }

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

  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents
