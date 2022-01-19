const fs = require('fs');
let input = fs.readFileSync('./dev/stdin').toString().trim().split('\n');

const n = Number(input.shift());
//let input = ['11', '1 4', '3 5', '0 6', '5 7', '3 8', '5 9', '6 10', '8 11', '8 12', '2 13', '12 14'];
//arr.sort((a, b) => a - b);
let table = new Array(n);
for(let i=0; i<n; i++){
    let [sp, ep] = input[i].toString().trim().split(' ').map(c => parseInt(c));
    table.push([sp, ep]);
}


table.sort((a,b) => {
    if (a[1] === b[1]) return a[0]-b[0];
    return a[1] - b[1];
});

let ep = table[0][1];
let cnt =1;
for (let i=1; i<n; i++) {
    if(table[i][0] >= ep) {
        cnt++;
        ep = table[i][1];
    }
}

console.log(cnt);
