#!/usr/bin/node
// reads  of a file
const fs = require('fs');

let filepath = '';
if (process.argv[2] !== undefined) {
  filepath = process.argv[2];
}
fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
