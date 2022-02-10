const express = require('express')
const app = express()
const port = 3000
var sh = require("shelljs");

app.get('/', (req, res) => {


    var cwd = sh.pwd();
    console.log(cwd);

    // const { spawn } = require('child_process');
    // const pyProg = spawn('python3', ['test.py']);

    // pyProg.stdout.on('data', function(data) {

    //     console.log(data.toString());
    //     res.write(data);
    //     res.end('end');
    // });
})
   


app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
