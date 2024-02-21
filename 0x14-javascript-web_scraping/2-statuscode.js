#!/usr/bin/node
// displays  status code of a GET 
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log('code:', response && response.statusCode);
});
