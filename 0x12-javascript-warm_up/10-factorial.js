#!/usr/bin/node
const myArgs = process.argv.slice(2);
const occurence = Number(myArgs[0]);
function factorial (occurence) {
  if (!occurence) {
    return 1;
  } else {
    let fact = 1;
    for (let i = 1; i <= occurence; i++) {
      fact *= i;
    }
    return fact;
  }
}
const ans = factorial(occurence);
console.log(ans);
