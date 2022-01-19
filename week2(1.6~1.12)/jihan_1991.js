const fs = require('fs');
let input = fs.readFileSync("input.txt").toString().trim().split('\n');

let cntnode = input.shift();
input = input.map(c=>c.trim().split(' '));

const getindex = (str) =>{
    for(let i = 0; i<cntnode; i++){
        if(input[i][0] == str){return i;}
    }
}

const getleftchild = (nodeindex) => {
    return input[nodeindex][1];
}

const getrightchild = (nodeindex) => {
    return input[nodeindex][2];
}

let preorderstr = '';
const preorder = (node_data) => {
    let left = getleftchild(getindex(node_data));
    let right = getrightchild(getindex(node_data));
    preorderstr+=node_data;
    if(left != '.'){
        preorder(left);
    }
    if(right != '.'){
        preorder(right);
    }
}

let inorderstr = '';
const inorder = (node_data) =>{
    let left = getleftchild(getindex(node_data));
    let right = getrightchild(getindex(node_data));
    if(left != '.'){
        inorder(left);
    }
    inorderstr+=node_data;
    if(right != '.'){
        inorder(right);
    }
}


let postorderstr = '';
const postorder = (node_data) => {
    let left = getleftchild(getindex(node_data));
    let right = getrightchild(getindex(node_data));
    if(left != '.'){
        postorder(left);
    }
    if(right != '.'){
        postorder(right);
    }
    postorderstr+=node_data;
}

preorder('A');
console.log(preorderstr);
inorder('A');
console.log(inorderstr);
postorder('A');
console.log(postorderstr);