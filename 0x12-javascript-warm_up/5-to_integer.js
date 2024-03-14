#!/usr/bin/node
const { argv } = require('process');
// because arguments are stored as strings:
const inputArg = Number(argv[2]);
// because conversion will return nan in case of not a number
if (!isNaN(inputArg)) {
  const myIntegr = Math.floor(inputArg);
  const myLine = 'My number: ' + myIntegr;
  console.log(myLine);
} else {
  console.log('Not a number');
}
