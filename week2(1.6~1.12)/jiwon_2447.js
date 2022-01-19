// const fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');   // input은 줄 단위로 끊어진 배열로 저장 및 string임.

let input = [
  '27'
]

let N = Number(input[0]); // 주어진 정수를 N에 저장
const arr = Array.from(Array(N), () => new Array(N).fill(' ')); // N*N 크기의 2차원 배열 생성 및 공백으로 초기화

const fill = (x, y) => {    // 단위 별을 찍어주는 함수 3*3의 반복문에서 가운데를 제외하고 별을 찍음
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      if (i === 1 && j === 1)
        continue;
      arr[x + i][y + j] = '*';
    }
  }
};
// ***  얘가 단위 별
// * *
// ***

const star = (x, y, n) => { // 시작x좌표, y좌표, 현재 깊이를 인자로 받음
  if (n === 3) {  // 깊이가 1일때(3의 1제곱) 단위 별 출력
    return fill(x, y);
  }
  for (let i = 0; i < 3; i++) { // 중심을 제외한 8개의 위치에서 재귀 호출
    for (let j = 0; j < 3; j++) {
      if (i === 1 && j === 1)
        continue;
      star(x + (n / 3) * i, y + (n / 3) * j, n / 3);  // x, y 좌표에서 단위/3 씩 이동한 좌표를 인자로
    }
  }
};

star(0, 0, N);  //0,0위치에서 star 호출

console.log(arr.map(c => c.join('')).join('\n'));
