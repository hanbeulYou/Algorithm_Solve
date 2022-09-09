#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

bool cmp(pair<string, int>a, pair<string, int>b){
    int cmp_result = a.first.compare(b.first);
    if(a.second < b.second)
        return true;
    else if(a.second == b.second && cmp_result < 0)
        return true;
    else
        return false;
}

int main(void){
    int N;
    int i;
    string str;
    vector<pair<string, int> > vec;

    cin >> N;
    for(i=0; i<N; i++){
        cin >> str;
        vec.push_back(make_pair(str, str.length()));
    }
    sort(vec.begin(), vec.end(), cmp);
    
    cout << vec[0].first << '\n';
    for(i=1; i<N; i++)
        if(vec[i].first.compare(vec[i-1].first)!=0)
            cout << vec[i].first << '\n';
    return 0;
}