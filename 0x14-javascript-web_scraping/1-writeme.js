#!/usr/bin/node
//  string to a file
const fs = require('fs');

let pathfile = '';
if (process.argv[2] !== undefined) {
  pathfile = process.argv[2];
}
fs.writeFile(pathfile, process.argv[3], 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
