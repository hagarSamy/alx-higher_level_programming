#!/usr/bin/node
const { argv } = require('process');
const x = Number(argv[2]);
function factorial (x) {
  if (isNaN(x) || x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
console.log(factorial(x));
