const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let m = input.shift();

let n = m.split(' ')[1];
m = m.split(' ')[0];

let array = [];
input.forEach(c=>{
  array.push(c.split(''));
})

function cntcng(arr,column,row){
  let arr_88 = [];
  let rowarr = [];
  let cng_W = 0;
  let cng_B = 0;
  for(let j = 0;j < 8; j++){
    for(let i = 0;i < 8; i++){
      rowarr.push(arr[column+j][row+i]);
    }
    arr_88.push(rowarr);
    rowarr = [];
  }
  arr_88.forEach((c1,i1)=>{
    if(i1%2 ==0){
      c1.forEach((c2,i2)=>{
        if(i2%2==0 && c2=='B'){cng_W++;}
        if(i2%2==1 && c2=='W'){cng_W++;}
      })
    }
    else{
      c1.forEach((c2,i2)=>{
        if(i2%2==0 && c2=='W'){cng_W++;}
        if(i2%2==1 && c2=='B'){cng_W++;}
      })
    }
  })
  arr_88.forEach((c1,i1)=>{
    if(i1%2 ==0){
      c1.forEach((c2,i2)=>{
        if(i2%2==0 && c2=='W'){cng_B++;}
        if(i2%2==1 && c2=='B'){cng_B++;}
      })
    }
    else{
      c1.forEach((c2,i2)=>{
        if(i2%2==0 && c2=='B'){cng_B++;}
        if(i2%2==1 && c2=='W'){cng_B++;}
      })
    }
  })
  return cng_W>cng_B? cng_B : cng_W;
}

let cngarr = [];

for(let i = 0; i < (m-7); i++){
  for(let j =0; j < (n-7); j++){
    cngarr.push(cntcng(array,i,j));
  }
}

let min = cngarr[0];
cngarr.forEach(c=>{
  if (c<min){min =c};
})

console.log(min);