const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

let num = Number(input[0]);
//let num = 27;
let k = 0;
while (1) {
  if(num / 3**k == 1) break;
  else k++;
}
let index = Array.from(Array(num), () => new Array(num).fill('0'));

let ans = '';

function countingStars(n) {
  if (!n) return;
  let min = 3**(n-1);
  let max = 2*min;
  for(let i=0; i<num; i++) {
    let iflag = i % (3**n);
    if (iflag >=min && iflag < max) {
      for(let j=0; j<num; j++) {
        let jflag = j % (3**n);
        if (jflag >=min && jflag < max) {
          index[i][j] = 1;
        }
      }
    }
  }
  countingStars(n-1);
  return;
}


countingStars(k);
printingStars();

function printingStars() {
    ans = '';
    for(let i=0; i<num; i++) {
      for(let j=0; j<num; j++) {
        if(index[i][j] == 1) ans += ' ';
        else ans += '*';
      }
      ans += '\n';
    }
    console.log(ans);
}


