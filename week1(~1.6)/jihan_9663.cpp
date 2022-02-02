#include <iostream>
#include <cstdlib>
using namespace std;

int N, cnt = 0;
int board[15]{};

bool promising(int rows){
    for(int i=0;i<rows;i++){
        if(board[rows] == board[i] || rows-i == abs(board[rows] - board[i])){
            return false;
        }
    }
    return true;
}

void confirm(int k){
    if (k==N){
        cnt++;
    }
    else{
        for(int i=0;i<N;i++){
            board[k] = i;
            if(promising(k)){
                confirm(k+1);
            }
        }
    }
}

int main(){
    cin>>N;
    confirm(0);
    cout<<cnt<<endl;
    return 0;
}

