#!/usr/bin/node
let biggest = 0;
const numberArray = [];
let i;

for (i = 2; i < process.argv.length; i++) {
  if (Number.isNaN(process.argv[i]) === false) {
    numberArray[i - 2] = parseInt(process.argv[i]);
  }
}

if (numberArray.length > 1) {
  biggest = Math.max.apply(null, numberArray);
  i = numberArray.indexOf(biggest);
  numberArray[i] = -Infinity;
  biggest = Math.max.apply(null, numberArray);
}
console.log(biggest);
