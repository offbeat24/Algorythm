const fs = require('fs');
let input = fs.readFileSync("input.txt").toString().trim().split('\n');

let cnt = Number(input.shift());
input = input
    .map(c=>c.trim().split(' ').map(Number))
    .sort((a,b)=>{return a[1] == b[1] ? a[0] - b[0] : a[1] - b[1];});

let ans = 0, temp = 0;
input.forEach(c=>{
    if(c[0]<temp) return;
    ans++;
    temp = c[1];
})

console.log(ans);