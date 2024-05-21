#!/usr/bin/node

const id = 18;
const request = require('request');
const movAPI = process.argv[2];
const fullUrl = `${movAPI}/${id}`
request(movAPI, (error, response, body) => {
  if (!error) {
    const bodyObj = JSON.parse(body);
    console.log(bodyObj);
  }
});
