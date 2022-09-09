#include <iostream>
using namespace std;

int main(){
    int N;
    cin >> N;
    for(int i=N/5; i>=0; i--){
        if((N-i*5)%3==0){
            cout << i + (N-i*5)/3;
            return 0;
        }
    }
    cout << "-1";
    return 0;
}