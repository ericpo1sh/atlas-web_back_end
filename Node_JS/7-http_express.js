// Create a more complex HTTP server using Express 
const express = require('express');
const fs = require('fs').promises;
const process = require('process');

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter(line => line.trim() !== '');
    const studentCount = lines.length - 1;
    const fields = {
        CS: [],
        SWE: [],
    };

    for (let i = 1; i < lines.length; i++) {
      const details = lines[i].split(',');
      const firstName = details[0].trim();
      const field = details[3].trim();

      if (field === 'CS') {
          fields.CS.push(firstName);
      } else if (field === 'SWE') {
          fields.SWE.push(firstName);
      }
    }

    let result = 'This is the list of our students\n';
    result += `Number of students: ${studentCount}\n`;
    result += `Number of students in CS: ${fields.CS.length}. List: ${fields.CS.join(', ')}\n`;
    result += `Number of students in SWE: ${fields.SWE.length}. List: ${fields.SWE.join(', ')}`;

    return result;
  } catch (err) {
    throw new Error('Cannot load the database');
}
}

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const result = await countStudents(process.argv[2]);
    res.send(result);
  } catch (error) {
    res.send(error.message);
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
