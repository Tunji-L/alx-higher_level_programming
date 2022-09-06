#!/usr/bin/node
const myArgs = process.argv.slice(2);

function add (a, b) {
  return a + b;
}

if (Number(myArgs[0]) && Number(myArgs[1])) {
  const result = add(Number(myArgs[0]), Number(myArgs[1]));
  console.log(result);
} else {
  console.log('NaN');
}
