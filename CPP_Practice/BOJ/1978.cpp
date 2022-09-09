#include <iostream>
using namespace std;

bool isPrimeNum(int num){
    int cnt = 0;
    for(int i=1;i<=num;i++)
        if(num%i==0) cnt++;
    if(cnt==2) return true;
    return false;
}

int main(void){
    int N, num;
    int result = 0;
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> num;
        if(isPrimeNum(num)) result++;
    }
    cout << result;
    return 0;
}