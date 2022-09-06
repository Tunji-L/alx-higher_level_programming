#!/usr/bin/node
const myArgs = process.argv.slice(2);
const size = Number(myArgs[0]);
if (size) {
  for (let i = 0; i < size; i++) {
    let k = '';
    for (let j = 0; j < size; j++) {
      k += 'X';
    }
    console.log(k);
  }
} else {
  console.log('Missing size');
}
