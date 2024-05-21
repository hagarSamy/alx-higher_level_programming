#!/usr/bin/node

const FilePath = process.argv[2];
const string = process.argv[3];
// importing the error method to be able to use it
// extract the error property from the object returned by require('console') and
// assign it to a new variable named error
const { error } = require('console');
const fs = require('fs');

fs.writeFile(FilePath, string, 'utf8', (err) => {
  if (err) {
    console.error(error);
  }
});
