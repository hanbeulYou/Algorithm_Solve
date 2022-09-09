#include <iostream>
#include <tuple>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

// tuple 이 왜 안읽히지? 일단 여기까지만 진행.
bool cmp(tuple<int, string, int>a, tuple<int, string, int>b){
    if(a.first < b.first)
        return true;
    elif(a.first == b.first)
    else
        return false;
}

int main(void){
    int N;
    int i;
    int age;
    string name;
    vector<tuple<int, string, int> > vec;

    cin >> N;
    for(i=0; i<N; i++){
        cin >> age >> name;
        vec.push_back(make_tuple(age, name, i));
    }
    sort(vec.begin(), vec.end(), cmp);
    
    for(i=0; i<N; i++)
        cout << vec[i].first << ' ' << vec[i].second << '\n';
    return 0;
}