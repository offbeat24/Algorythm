#include <iostream>
using namespace std;

int main(){
    int testcase;
    cin >> testcase;

    int cases[testcase][2]{};
    int arr_apart[15][14]{};

    for (int i = 0; i < 14; i++){
        arr_apart[0][i] = i+1;
    }

    for (int row = 1; row < 15; row++){
        arr_apart[row][0] = 1;
        for(int col = 1; col < 14; col++){
            arr_apart[row][col] = arr_apart[row-1][col] + arr_apart[row][col-1];
        }
    }
    
    /*for(int row = 0; row < 15; row++){
        for(int col = 0; col < 14; col++){
            cout<<arr_apart[row][col]<<" ";
        }
        cout<<endl;
    }*/

    for (int i = 0; i < testcase; i++){
        int k, n;
        cin >> k >> n;
        cout<< arr_apart[k][n-1] << endl;
    }

    return 0;
}