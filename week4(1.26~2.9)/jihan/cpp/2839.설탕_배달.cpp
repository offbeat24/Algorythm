#include <iostream>
using namespace std;

int main(){
  int N,bag5 = 0,mod = 0;
  cin>>N;
  bag5 = N/5;
  while(bag5>=0){
    mod = N - (bag5*5);
    if(mod%3 == 0){break;}
    bag5--;    
  }
  if(mod%3 != 0){cout<<-1;}
  else{cout<<bag5+((int)mod/3);}
}
