#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (!myArgs[0] || myArgs.length === 1) {
  console.log(0);
} else {
  myArgs.sort();
  myArgs.reverse();
  console.log(myArgs[1]);
}
