#!/usr/bin/node
const { argv } = require('node:process');
// a value is undefined if the var is there but giveN no vALUE
if (typeof argv[2] === 'undefined') {
  console.log('No argument');
} else {
  let i = 2;
  while (argv[i]) {
    console.log(argv[i]);
    i++;
  }
}
