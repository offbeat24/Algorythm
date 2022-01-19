const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');   // input은 줄 단위로 끊어진 배열로 저장 및 string임.


// let input = [
//   '2',
//   '5',
//   '3 2',
//   '1 4',
//   '4 1',
//   '2 3',
//   '5 5',
//   '7',
//   '3 6',
//   '7 3',
//   '4 2',
//   '1 4',
//   '5 7',
//   '2 5',
//   '6 1'
// ];    // 4 3

let T = input.shift();
let arr = []
for (let i = 0; i < T; i++){
  let N = input.shift();
  let arr2 = input.splice(0, N).map(c=> c.split(' ').map(d=>parseInt(d)));  // 각 테스트별 지원자 수만큼 자름

  // for (let j = 0; j < N; j++){
  //   arr2.push(input.shift().split(' ').map(c => parseInt(c)));
  // }  // shift()의 실행속도때문에 시간초과 발생

  arr2.sort(([a, b], [c, d]) => {
    return a === c ? b - d : a - c; // 서류심사 성적 기준 오름차순 정렬, 같은성적은 면접성적 오름차순 정렬
  })
  arr.push(arr2);
}

let ret = [];
arr.forEach(c => {
  let temp = 1000001; // 임시 등수(최저등수)
  let num = 0;  // 합격자 수
  c.forEach(([a,b]) => { // 서류심사 기준 오름차순이기에 면접 성적만 비교
    if (temp < b)   // 면접성적이 이전 합격자 등수보다 낮을 시 불합격
      return;
    temp = b;
    num++;
  })
  ret.push(num);
})

console.log(ret.join('\n').trim());
