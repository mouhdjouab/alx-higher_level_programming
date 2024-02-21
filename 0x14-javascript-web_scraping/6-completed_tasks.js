#!/usr/bin/node
// totals tasks completed per user_id,  with 0
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const tasksList = JSON.parse(body);
  const usersTotals = {};
  for (const task of tasksList) {
    if (task.completed) {
      if (task.userId in usersTotals) {
        usersTotals[task.userId] += 1;
      } else {
        usersTotals[task.userId] = 1;
      }
    }
  }
  console.log(usersTotals);
});
