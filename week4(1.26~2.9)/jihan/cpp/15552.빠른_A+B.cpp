#include <iostream>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int T,A,B;
  cin>>T;
  for(int i = 0; i<T; i++){
    cin>>A;
    cin>>B;
    cout<<A+B<<"\n";
  }
}