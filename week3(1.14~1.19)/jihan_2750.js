const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

input.shift();
input.sort((x,y)=>{return x-y;})
console.log(input.join('\n'));