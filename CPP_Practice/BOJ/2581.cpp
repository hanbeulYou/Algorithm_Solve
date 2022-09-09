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
    int N, M;
    int min = 0, sum = 0;
    bool flag = false;
    cin >> M >> N;
    for(int i=M; i<=N; i++){
        if(isPrimeNum(i)){
            sum += i;
            if(!min) min=i;
            flag = true;
        }
    }
    if(flag) cout << sum << '\n' << min;
    else cout << "-1";
    return 0;
}