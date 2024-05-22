#!/usr/bin/node

const request = require('request');
const movAPI = process.argv[2];
// const fullUrl = `${movAPI}/${id}`
request(movAPI, (error, response, body) => {
  if (!error) {
    let count = 0;
    const films = JSON.parse(body).results;
    films.forEach(film => {
      if (film.characters.some(characterUrl => characterUrl.endsWith('/18/'))) {
        count++;
      }
    });
    console.log(count);
  }
});
