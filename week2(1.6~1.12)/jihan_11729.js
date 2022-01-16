const fs = require('fs');
const input = Number(fs.readFileSync('input.txt').toString().trim());
let cnt = 0;
let list = '';
function hanoi(n,start,end,etc){
  if(n==0)return;
  hanoi(n-1,start,etc,end);
  list+= '\n'+ start + ' ' + end;
  cnt++;
  hanoi(n-1,etc,end,start);
}
hanoi(input,'1','3','2');
console.log(cnt.toString()+list);