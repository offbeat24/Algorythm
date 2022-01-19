const fs = require('fs');
const input = Number(fs.readFileSync('input.txt').toString().trim());

const cnt = parseInt(Math.log(input)/Math.log(3));
//로그가 자연로그 밖에 없어서 밑변환으로 지수값 반환
let str = '*'

const astro = (x) => {
  if(x==0){return;}  // 종료조건
  let str1 = str.split('\n').map(c=>c+c+c).join('\n').trim();
  
  let str2 = str.split('\n').map(c=>c+(' '.repeat(str.split('\n')[0].length))+c).join('\n').trim();
  
  str = str1+('\n')+str2+('\n')+str1;
  astro(x-1);  // 재귀호출
}

astro(cnt);
console.log(str.split('\n').map(c=>c.trim()).join('\n'));