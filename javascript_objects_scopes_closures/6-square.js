#!/usr/bin/node
const previousclass = require('./5-square');

class Square extends previousclass {
  charPrint (c) {
    const char = c || 'X';  // Default to 'X' if c is undefined
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;

