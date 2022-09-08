#include <iostream>
using namespace std;

int main(void){
    int k, q, r, b, n, p;
    std::cin >> k >> q >> r>> b>> n>> p;
    std::cout << (1-k) << ' ' << (1-q) << ' ' << (2-r) << ' ' << (2-b) << ' ' << (2-n) << ' ' << (8-p);
    return 0;
}