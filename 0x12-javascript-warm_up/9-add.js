#!/usr/bin/node

const arg1 = Number(process.argv[2]);
const arg2 = Number(process.argv[3]);

if (!arg1 || !arg2) {
  console.log('NaN');
} else {
  console.log(arg1 + arg2);
}
