#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
int main(void){
    int N;
    int i;
    int item;
    int sum = 0;
    int max, min;
    int arr[8001] = {0,};
    int mode = 0, mode_idx = -4001;
    vector<int> v;
    cin >> N;
    for(i=0; i<N; i++){
        cin >> item;
        sum += item;
        arr[item+4000]++;
        v.push_back(item);
    }
    sort(v.begin(), v.end());
    max = *max_element(v.begin(), v.end());
    min = *min_element(v.begin(), v.end());

    for(i=0; i<8001; i++)
        if(mode < arr[i])
            mode = arr[i];
    
    for(i=0; i<8001; i++)
        if(mode == arr[i]){
            if(mode_idx == -4001)
                mode_idx = i - 4000;
            else{
                mode_idx = i - 4000;
                break;
            }
        }

    if(round(1.0*sum/N) == -0)
        cout << 0 << '\n';
    else
        cout << round(1.0*sum/N) << '\n';
    cout << v[int(N/2)] << '\n';
    cout << mode_idx << '\n';
    cout << abs(max-min) << '\n';
    return 0;
}