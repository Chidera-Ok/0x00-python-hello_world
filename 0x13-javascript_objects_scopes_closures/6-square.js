#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0, s; i < this.heigth; i++) {
      s = '';
      for (let k = 0; k < this.width; k++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Square;
