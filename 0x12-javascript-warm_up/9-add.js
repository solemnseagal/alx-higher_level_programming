#!/usr/bin/node
const args = process.argv;
const A = Number(args[2]);
const B = Number(args[3]);
if (A !== null && B !== null) {
  console.log(add(A, B));
} else {
  console.log('NaN');
}

function add (a, b) {
  return (a + b);
}
