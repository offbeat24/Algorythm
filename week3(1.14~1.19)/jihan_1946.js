const fs = require('fs');
let input = fs.readFileSync("input.txt").toString().trim().split('\n');
let testcase = Number(input.shift());
input = input.map(c=>c.trim().split(' ').map(Number));

//console.log(input);

let index = 0;
let array = [];

const count = (array,length) => {
    array.sort((a,b)=>{return a[0]-b[0];})

    for(let i = 1; i<array.length; i++){
        for(let j = 0; j<i; j++){
            if(array[j][1]<array[i][1]){length--;break;}
        }
    }

    console.log(length);
}

for(let i = 0; i<testcase; i++){
    temp = input[index][0];
    //console.log(temp);
    let start = index+1, end = index+temp;
    
    for(let j = start; j <= end; j++){
        array.push(input[j]);
    }
    count(array,temp);
    //console.log(array);
    index+=temp+1;
    array = [];
}