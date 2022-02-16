#include <iostream>
using namespace std;

int main(){
  int L;
  cin>>L;
  char string[L];
  cin>>string;
  int prime = 1234567891;

  long long hashing = 0;
  long long temp = 0;
  long long pow = 1;

  for(int i = 0; i < L; i++){
    pow%=prime;
    temp = (((int)string[i]-96)*pow)%prime;
    hashing+=temp;
    hashing%=prime;
    pow*=31;
  }

  cout<<hashing;
}