#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

  int array[10000] = {0,};
  int N, temp, max = -1;
  cin>>N;

  for(int i = 0; i < N; i++){
    cin>>temp;
    array[temp-1]++;
    if(temp>max){
      max = temp;
    }
  }

  for(int i = 0; i < max; i++){
    while(array[i]--){
      cout<<i+1<<"\n";
    }
  }
}