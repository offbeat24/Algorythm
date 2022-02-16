#include <iostream>
#include <algorithm>
using namespace std;

int quicksort(int array[], int start, int end){
  if(start>=end) {return 0;} // 배열 길이가 0 또는 1인 경우 리턴

  int pivot = array[start];
  int tmp_l = start + 1;
  int tmp_r = end;
  //array의 첫번째 값을 pivot으로, 그 다음 인덱스를 left temp값, 마지막 인덱스를 right temp값으로 할당

  while(tmp_l<=tmp_r){  //인덱스 포인터가 엇갈릴 때까지 반복
    while(array[tmp_l]<=pivot && tmp_l<end){
      tmp_l++;
    }
    while(array[tmp_r]>pivot && tmp_r>start){
      tmp_r--;
    }
    if(tmp_l>tmp_r){swap(array[start],array[tmp_r]);}//엇갈리면, pivot값을 올바른 위치로 swap
    else{swap(array[tmp_l],array[tmp_r]);}//왼쪽값 중 pivot보다 큰 값, 오른쪽값 중 pivot보다 작은 값을 발견할 때마다 swap해줌.
  }  

  quicksort(array,start,tmp_r-1);
  quicksort(array,tmp_r+1,end);
  //모든 분할구간에서 실행되도록 재귀호출

  return 0;
}

int binarysearch(int array[], int len, int target){
  int low = 0;
  int high = len-1;
  int mid;

  while(high>=low){
    mid = (low+high)/2;

    if(array[mid]==target){
      return 1;
    }
    else if(array[mid]>target){
      high = mid-1;
    }
    else if(array[mid]<target){
      low = mid+1;
    }
  }

  return 0;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
  int n = 0;
  cin>>n;
  int target[n]{};
  for(int i = 0; i<n; i++){
    cin>>target[i];
  }

  int m = 0;
  cin>>m;
  int finding[m]{};
  for(int i = 0; i<m; i++){
    cin>>finding[i];
  }

  quicksort(target,0,n-1);

  for(int i = 0; i<m; i++){
    cout<<binarysearch(target, n, finding[i])<<"\n";
  }
}