#!/usr/bin/node

const { exit } = require('process');

const url = process.argv[2];
fs = require('fs');
request = require('request');

request(url, (error, response, body) => {
  if (error) {
    exit(1)
  }
  console.log('code: ', response.statusCode);
});
