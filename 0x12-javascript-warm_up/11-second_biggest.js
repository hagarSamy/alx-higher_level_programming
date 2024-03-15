#!/usr/bin/node
const { argv } = require('process');
const len = argv.length;
if (len <= 3) {
  console.log('0');
} else {
  let x, max, secMax;
  max = Number(argv[2]);
  secMax = Number(argv[2]);
  for (let i = 3; i < len; i++) {
    x = Number(argv[i]);
    if (x > max) {
      max = x;
    }
    if (secMax < x && x < max) {
      secMax = x;
    }
  }
  console.log(secMax);
}
