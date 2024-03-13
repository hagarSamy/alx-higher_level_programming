#!/usr/bin/node
const { argv } = require('node:process');
// a value is undefined if the var is defined but given no vALUE
if (typeof process.argv[2] === 'undefined') {
  console.log('No argument');
} else {
  let i = 2;
  while (process.argv[i]) {
    console.log(process.argv[i]);
    i++;
  }
}
