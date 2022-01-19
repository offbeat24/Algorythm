// const fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');   // input은 줄 단위로 끊어진 배열로 저장 및 string임.

let input = [
  '7',
  'A B C',
  'B D .',
  'C E F',
  'E . .',
  'F . G',
  'D . .',
  'G . .',
]

input.shift();  // 입력값 첫 내용 삭제
let dict = {};  // 딕셔너리 생성
input.map(c => {
  return c.split(' ');
}).forEach(c => { // 각 줄에 대해서
  dict[c.shift()] = c;  //  딕셔너리에 shift()한 값을 key, 남은 배열을 value로 갖는 pair 추가
});

console.log(dict);
const preorder = (c) => { // c는 현재 조회하려는 값
  if (c === '.') {  // . 을 받으면 빈 문자열 리턴
    return '';
  }
  return c + preorder(dict[c][0]) + preorder(dict[c][1]); // 현재 조회하는 값과, 왼쪽자식, 오른쪽 자식 순회
};

const inorder = (c) => {
  if (c === '.') {
    return '';
  }
  return inorder(dict[c][0]) + c + inorder(dict[c][1]);
};

const postorder = (c) => {
  if (c === '.') {
    return '';
  }
  return postorder(dict[c][0]) + postorder(dict[c][1]) + c;
};

console.log(preorder('A'));
console.log(inorder('A'));
console.log(postorder('A'));
