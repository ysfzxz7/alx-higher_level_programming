#!/usr/bin/node

const arg1 = Math.floor(Number(process.argv[2]));

console.log(arg1 || 'Not a number');
