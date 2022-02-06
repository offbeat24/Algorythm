const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

input.shift();

let arr = input.map(c=>parseInt(c));

arr.sort((a, b) => a - b);

for (let i=0; i<arr.length; i++) console.log(arr[i]);
