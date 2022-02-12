#include <iostream>
using namespace std;

int fact(int num){
  if(num==0) return 1;
  return num*fact(num-1);
}

int main(){
  int N,K;
  cin>>N>>K;
  int combi;
  combi = fact(N)/(fact(K)*fact(N-K));
  cout<<combi<<endl;
}