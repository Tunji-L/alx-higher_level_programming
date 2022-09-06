#!/usr/bin/node
const myArgs = process.argv.slice(2);
const occurence = Number(myArgs[0]);
if (occurence) {
  for (let i = 0; i <= occurence; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
