#!/usr/bin/node

const epId = process.argv[2];
const request = require('request');
const movAPI = `https://swapi-api.alx-tools.com/api/films/${epId}`;

request(movAPI, (error, response, body) => {
  if (!error) {
    const bodyObj = JSON.parse(body);
    console.log(bodyObj.title);
  }
});
