#!/usr/bin/node

const FilePath = process.argv[2];
const string = process.argv[3];
// importing the error method to be able to use it
const { error } = require('console');
const fs = require('fs');

fs.writeFile(FilePath, string, 'utf8', (err) => {
  if (err) {
    console.error(error);
  }
});
