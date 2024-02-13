#!/usr/bin/node

const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c) {
    const char = c || 'X';
    let line = '';
    for (let i = 0; i < this.width; i++) line += char;
    for (let j = 0; j < this.height; j++) console.log(line);
  }
}

module.exports = Square;
