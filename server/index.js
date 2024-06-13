const express = require('express');
const { PythonShell } = require('python-shell');
const path = require('path');

async function checkSpamHandler(req, res) {
  const input = req.body;
  console.log('Input:', input);

  try {
    const result = await PythonShell.run('predict.py', {
      mode: 'text',
      scriptPath: '../model',
      args: [input],
    });

    if (result[0] === '1') {
      console.log('Result: SPAM');
      return res.status(200).send('1');
    } else {
      console.log('Result: HAM');
      return res.status(200).send('0');
    }
  } catch (error) {
    console.error('Error:', error);
    return res.status(500).send('-1');
  }
}

const app = express();
app.use(express.text());
app.use(express.static(path.join(__dirname, 'public')));

app.post('/check-spam', checkSpamHandler);
app.get('*', (_, res) => {
  res.redirect('/');
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
  console.log('Frontend available at http://localhost:3000');
});
