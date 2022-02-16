const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const num = Number(input[0]);
let node = [];
let tree = {};
for(let i=1; i<=num; i++) {
    node = input[i].split(' ');
    tree[node[0]] = [node[1], node[2]];
}

let ans = '';
function preorder(node) {
    if (node == '.') return;
    ans += node;
    let [left, right] = tree[node];
    preorder(left);
    preorder(right);
}
function inorder(node) {
    if (node == '.') return;
    let [left, right] = tree[node];
    inorder(left);
    ans += node;
    inorder(right);
} 

function postorder(node) {
    if (node == '.') return;
    let [left, right] = tree[node];
    postorder(left);
    postorder(right);
    ans += node;
} 

preorder('A');
ans += '\n';
inorder('A');
ans += '\n';
postorder('A');
ans += '\n';

console.log(ans);