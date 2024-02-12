#!/usr/bin/node

const arg1 = Math.floor(Number(process.argv[2]));

console.log(isNaN(arg1) ? 'My number: ' + arg1 : 'Not a number');
