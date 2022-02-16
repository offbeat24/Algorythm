#include <iostream>
#include <algorithm>
using namespace std;

int GCD(int a,int b){
  if(b>a){
    swap(a,b);
  }
  int temp;
  while(b!=0){
    temp = a%b;
    a = b;
    b = temp;
  }
  return a;
}

int main(){
  int a, b;
  cin>>a>>b;
  cout<<GCD(a,b)<<endl;
  cout<<(a*b)/GCD(a,b)<<endl;
}