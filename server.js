const express = require('express');
const app = express();
app.use(express.text({ type: '*/*' }));

let cmd = { task: "idle" };
let output = "";

app.get('/cmd', (req, res) => res.json(cmd));
app.post('/upload', (req, res) => {
  if (req.query.token === 'x7G!qL2@') {
    output = req.body;
    res.send('OK');
  } else {
    res.status(403).send('DENIED');
  }
});
app.get('/output', (req, res) => res.send(output));

app.listen(10000, () => console.log('Running'));
