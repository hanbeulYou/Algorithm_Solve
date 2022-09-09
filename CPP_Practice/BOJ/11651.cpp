#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(pair<int, int>a, pair<int, int>b){
    if(a.second < b.second)
        return true;
    else if(a.second == b.second && a.first < b.first)
        return true;
    else
        return false;
}

int main(void){
    int N;
    int i;
    int x, y;
    vector<pair<int, int> > vec;

    cin >> N;
    for(i=0; i<N; i++){
        cin >> x >> y;
        vec.push_back(make_pair(x, y));
    }
    sort(vec.begin(), vec.end(), cmp);
    for(i=0; i<N; i++)
        cout << vec[i].first << ' ' << vec[i].second << '\n';
    return 0;
}