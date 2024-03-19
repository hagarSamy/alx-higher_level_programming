#!/usr/bin/node
// using a different name for imported class
// to avoid conflicts
const PSquare = require('./5-square.js');
class Square extends PSquare {
  charPrint (c) {
    if (c) {
      let i, x, rec;
      for (i = 0; i < this.height; i++) {
        rec = '';
        for (x = 0; x < this.width; x++) {
          rec += c;
        }
        console.log(rec);
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
