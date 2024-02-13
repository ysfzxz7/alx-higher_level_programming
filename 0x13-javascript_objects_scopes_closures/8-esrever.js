#!/usr/bin/node

// this func to reverse a function
exports.esrever = function (list) {
  if (!list) return (0)
  let reversed = [];
  for (let i = 0; i < list.length; i++) reversed.unshift(list[i]);
  return (reversed)
} 
