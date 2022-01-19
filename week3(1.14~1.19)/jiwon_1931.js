const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');   // input은 줄 단위로 끊어진 배열로 저장 및 string임.

// let input = ['11', '2 4','1 4', '3 5', '0 6', '5 7', '3 8', '5 9', '6 10', '8 11', '8 12', '2 13', '12 14'];
input.shift();
input = input.map(c => c.split(' ').map(d => parseInt(d))).sort((a, b) => {
  if (a[1] !== b[1])
    return a[1] - b[1];
  else
    return a[0] - b[0];
}); // 끝나는 시간 오름차순, 끝나는 시간이 같으면 시작하는 시간 오름차순 정렬

let ret = 0, temp = 0; // 회의 갯수, 마지막 회의가 끝난 시간

input.forEach(([a, b]) => {
  if (a < temp) // 회의 시작시간이 마지막 회의가 끝난 시간보다 빠르면 return
    return;
  ret++;
  temp = b;
})
console.log(ret);
