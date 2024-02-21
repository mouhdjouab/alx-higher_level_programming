#!/usr/bin/node
// uses Star Wars API to display amount of films featuring
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const movies = JSON.parse(body).results;
  const wedgeId = 18;
  let counter = 0;
  for (const film of movies) {
    for (const url of film.characters) {
      if (url.includes(
        `/api/people/${wedgeId}/`)) {
        counter += 1;
      }
    }
  }
  console.log(counter);
});
