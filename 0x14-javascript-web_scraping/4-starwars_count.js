#!/usr/bin/node

const request = require('request');
const movAPI = process.argv[2];
// const fullUrl = `${movAPI}/${id}`
request(movAPI, (error, response, body) => {
  if (!error) {
    let count = 0;
    const films = JSON.parse(body).results;
    films.forEach(film => {
      // some: checks if at least one element in the array passes the test implemented 
      if (film.characters.some(characterUrl => characterUrl.endsWith('/18/'))) {
        count++;
      }
    });
    console.log(count);
  }
});
