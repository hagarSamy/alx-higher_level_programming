#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  const sum = {};
  if (!error) {
    const todos = JSON.parse(body);
    todos.forEach(task => {
      if (task.completed) {
        if (!sum[task.userId]) {
          sum[task.userId] = 0;
        }
        sum[task.userId]++;
      }
    });
    console.log(sum);
  }
});
