#include <iostream>
#include <algorithm>
using namespace std;

int heap_sort(int heap[], int len){
    for(int i = 1; i < len; i++){
        int temp = i;
        while(temp>=0){
            int root = (temp-1) / 2;
            if(heap[root] < heap[temp]){
                swap(heap[root],heap[temp]);
            }
            temp = root;
        }
    }

    for(int i = len - 1; i>=0; i--){
        swap(heap[0],heap[i]);
        int root = 0, temp = 1;
        while(temp<=i){
            temp = 2*root + 1;
            if(temp<i-1 && heap[temp] < heap[temp+1]){
                temp++;
            }
            if(temp<i && heap[root] < heap[temp]){
                swap(heap[root],heap[temp]);
            }
            root = temp;
        }
    }
    return 0;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int N;
    cin>>N;
    int heap[N] = {0,};
    for(int i = 0; i < N; i++){
        cin>>heap[i];
    }

    heap_sort(heap,N);

    for(int i = 0; i < N; i++){
        cout<<heap[i]<<"\n";
    }
}