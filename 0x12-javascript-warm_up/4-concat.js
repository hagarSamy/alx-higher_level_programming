#!/usr/bin/node
const { argv } = require('node:process');
const myLine = argv[2] + ' is ' + argv[3];
console.log(myLine);
