// 5. Create a more complex HTTP server using Node's HTTP module 
const http = require('http');
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

const hostname = '127.0.0.1';
const port = '1244'

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  var url = req.url;
  if (url === '/') {
    res.end('Hello Holberton School!')
  }
  if (url === '/students') {
    try {
      const result = await countStudents(process.argv[2]);
      res.end(result);
    } catch (error) {
      res.end(`${error.message}`);
    }
  }
})

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
