#!/usr/bin/node
// using Star Wars API
const request = require('request');

const moviessURL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(moviessURL, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const url_list = JSON.parse(body).characters;
  for (const url of url_list) {
    request(url, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
