#!/usr/bin/node

const x = process.argv[2];
if (x < 0 || isNaN(x)) console.log('Missing number of occurrences');
for (let i = 0; i < x; i++) console.log('C is fun');
