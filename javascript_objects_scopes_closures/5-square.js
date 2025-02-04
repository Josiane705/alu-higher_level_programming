#!/usr/bin/node
const Rectangle = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = 0;
      this.height = 0;
    }
  }

  print () {
    if (this.width === 0 || this.height === 0) return;

    let prints = '';
    for (let xx = 0; xx < this.height; xx++) {
      for (let yy = 0; yy < this.width; yy++) {
        prints += 'X';
      }
      console.log(prints);
      prints = '';
    }
  }

  rotate () {
    const p = this.width;
    this.width = this.height;
    this.height = p;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};

module.exports = Rectangle;

