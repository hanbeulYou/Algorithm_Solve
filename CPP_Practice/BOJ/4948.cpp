#include <iostream>
#include <cmath>
using namespace std;

int main(void){
    int N;
    int i, j;
    int result;
    int max_N = 123456*2+1;
    bool prime_arr[max_N];
    fill_n(prime_arr, max_N, true);

    prime_arr[1] = false;
    for(i=2; i<=sqrt(max_N); i++){
        if(prime_arr[i]==true){
            j = i*2;
            while(j<=max_N){
                prime_arr[j] = false;
                j+=i;
            }
        }
    }

    while(1){
        cin >> N;
        if(N==0) return 0;
        result = 0;
        for(i=N+1; i<=N*2; i++)
            if(prime_arr[i]) result++;
        cout<<result<<'\n';
    }
}