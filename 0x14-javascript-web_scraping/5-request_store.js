#!/usr/bin/node
// GETs  of a web page and store in a file
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let filepath = '';
  if (process.argv[3] !== undefined) {
    filepath = process.argv[3];
  }
  fs.writeFile(filepath, body, 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
