const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello from the Backend!');
});

app.get('/greet', (req, res) => {
  res.send('Hello, world!');
});

app.listen(port, () => {
  console.log(`Backend app listening at http://localhost:${port}`);
});
