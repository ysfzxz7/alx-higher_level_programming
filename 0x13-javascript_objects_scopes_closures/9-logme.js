#!/usr/bin/node
// print orderly
let counter = 0;
exports.logMe = function (item) {
  console.log(counter + ': ' + item);
  counter++;
};
