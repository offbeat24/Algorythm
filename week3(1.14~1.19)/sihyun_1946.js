const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = ['2', '5','3 2','1 4','4 1','2 3','5 5','7','3 6','7 3','4 2','1 4','5 7','2 5','6 1'];
const n = Number(input.shift());

for(let i=0; i<n; i++) {
    let v = Number(input.shift());
    let score = [];
    for(let j=0; j<v; j++) {
        let [doc, inv] = input[j].toString().trim().split(' ').map(Number);
        score.push([doc, inv]);
    }

    score.sort((a,b) => a[0]-b[0]);

    let cnt = 1;
    let max = score[0][1];
    for(let i=1; i<v; i++) {
        if(score[i][1] > max) continue;
        else{
            cnt++;
            max = score[i][1];
        } 
    }
    console.log(cnt);
    input.splice(0, v);
}