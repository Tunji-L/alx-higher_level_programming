#!/usr/bin/node
const myArgs = process.argv.slice(2).map(occ => Number(occ));
if (!myArgs[0] || myArgs.length === 1) {
  console.log(0);
} else {
  myArgs.sort((a, b) => a - b);
  myArgs.reverse();
  console.log(myArgs[1]);
}
