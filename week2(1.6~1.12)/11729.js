const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const plates = Number(input[0]);
let cnt = 0;
let ans = '';
function countingHanoi(n, from, to, temp) {
  if(!n) return;
  countingHanoi(n-1, from, temp, to);
  ans += from + ' ' + to + '\n';
  cnt++;
  countingHanoi(n-1, temp, to, from);
}

countingHanoi(plates,1,3,2);
console.log(cnt);
console.log(ans);