#!/usr/bin/node
// process is an object and argv is a propery of it
// and that's how i get the argv array
const { argv } = require('node:process');
const len = argv.length;
switch (len) {
  case 2:
    console.log('No argument');
    break;
  case 3:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
    break;
}
