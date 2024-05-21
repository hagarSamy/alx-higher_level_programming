#!/usr/bin/node

const FilePath = process.argv[2];
const string = process.argv[3];
const { error } = require('console');
const fs = require('fs');

fs.writeFile(FilePath, string, 'utf8', (err) => {
  if (err) {
    console.error(error);
  }
});
