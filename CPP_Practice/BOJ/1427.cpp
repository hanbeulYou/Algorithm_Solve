#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void){
    int N;
    int cnt = 0;
    vector<int> arr;

    cin >> N;
    while(N>0){
        cnt++;
        arr.push_back(N%10);
        N/=10;
    }
    sort(arr.begin(), arr.end());
    for(int i=cnt-1; i>=0; i--)
        cout << arr[i];
    return 0;
}