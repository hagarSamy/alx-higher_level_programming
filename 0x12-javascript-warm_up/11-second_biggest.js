#!/usr/bin/node
const { argv } = require('process');
const len = argv.length;
if (len <= 3) {
  console.log('0');
} else {
  let x, max, secMax;
  max = 0;
  secMax = 0;
  for (let i = 2; i < len; i++) {
    x = Number(argv[i]);
    if (x > max) {
      // to keep secMax updated alongside the mx
      secMax = max;
      max = x;
    }
    if (secMax < x && x < max) {
      // to update secMax even if max isn't updated for an iteration
      secMax = x;
    }
  }
  console.log(secMax);
}
