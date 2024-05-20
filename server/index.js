const express = require('express');
const { PythonShell } = require('python-shell');

async function checkSpamHandler(req, res) {
  const input = req.body;
  console.log('Input:', input);
  const result = await PythonShell.run('predict.py', {
    mode: 'text',
    scriptPath: '../dist',
    args: [input],
  });

  if (result[0] === '1') {
    console.log('Result: SPAM');
    return res.send('Spam detected!');
  } else {
    console.log('Result: HAM');
    return res.send('Not spam!');
  }
}

const app = express();
app.use(express.text());

app.post('/check-spam', checkSpamHandler);
app.use('/', (req, res) => {
  return res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
