#!/usr/bin/node
const { argv } = require('process');
const x = Number(argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  let h, w;
  for (h = 0; h < x; h++) {
    w = '';
    for (let i = 0; i < x; i++) {
      w += 'X';
    }
    console.log(w);
  }
}
