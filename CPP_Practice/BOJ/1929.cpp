#include <iostream>
using namespace std;

int main(void){
    int N, M;
    int i;
    bool prime_arr[1000001];
    fill_n(prime_arr, 1000001, true);

    prime_arr[1] = false;
    for(i=2; i<=1000; i++){
        if(prime_arr[i]==true){
            int j = i*2;
            while(j<=1000000){
                prime_arr[j] = false;
                j+=i;
            }
        }
    }

    cin >> M >> N;
    for(int i=M; i<=N; i++)
        if(prime_arr[i]) cout << i << '\n';
    return 0;
}