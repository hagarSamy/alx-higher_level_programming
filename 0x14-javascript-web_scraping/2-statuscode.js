#!/usr/bin/node

const url = process.argv[2];
fs = require('fs');
request = require('request');

request(url, (error, response, body) => {
  console.log('code: ', response.statusCode);
});
