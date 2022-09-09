#include <iostream>
using namespace std;

int main(void){
    int T;
    int N;
    int i, j;
    bool prime_arr[10001];
    fill_n(prime_arr, 10001, true);

    prime_arr[1] = false;
    for(i=2; i<=100; i++){
        if(prime_arr[i]==true){
            j = i*2;
            while(j <= 10000){
                prime_arr[j] = false;
                j+=i;
            }
        }
    }
    
    cin >> T;
    for(i=0; i<T; i++){
        cin >> N;
        for(j=N/2; j>=2; j--){
            if(prime_arr[j] && prime_arr[N-j]){
                cout << j << ' ' << N-j << '\n';
                break;
            }
        }
    }
    return 0;    
}