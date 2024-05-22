#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, body) => {
  if (!error) {
    const fs = require('fs');
    fs.writeFileSync(file, body, 'utf8');
  }
});
