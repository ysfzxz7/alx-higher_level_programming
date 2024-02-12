#!/usr/bin/node

exports.callMeMoby = function (x, add) {
  for (let i = 0; i < x; i++) {
    add();
  }
};
