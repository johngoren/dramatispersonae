const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
    const { spawn } = require('child_process');
    const pyProg = spawn('python', ['./../main.py'])

    pyProg.stdout.on('data', function(data) {
        console.log(data.toString());
        res.write(data);
        res.end('end');
    })
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})