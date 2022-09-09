#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void){
    int N;
    int i;
    int item;

    vector<int> v;
    cin >> N;
    for(i=0; i<N; i++){
        cin >> item;
        v.push_back(item);
    }
    sort(v.begin(), v.end());
    //sort(v.begin(), v.end(), [](int a, int b) { return a > b;});
    for(i=0; i<N; i++)
        cout << v[i] << '\n';
    return 0;
}