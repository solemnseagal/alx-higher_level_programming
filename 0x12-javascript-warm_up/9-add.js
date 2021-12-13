#!/usr/bin/node
const args = process.argv;
let A = Number(args[2]);
let B = Number(args[3]);
if (A !== null && B !== null) {
  console.log(add(A, B));
} else {
  console.log('NaN');
}

function add (a, b) {
  return (a + b);
}
