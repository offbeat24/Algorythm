const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');   // input은 줄 단위로 끊어진 배열로 저장 및 string임.

// let input = ['5', '5', '2', '3', '4', '1', '7', '6', '11'];

input.shift();
input.sort((a, b) => {
  return a - b
});

console.log(input.join('\n').trim());
