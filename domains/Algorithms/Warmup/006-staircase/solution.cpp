#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  int n, h;
  cin >> n;
  h = n-1;
  while(h >= 0) {
    for (int i = 0; i < n; ++i) {
      if(i < h)
        cout << ' ';
      else
        cout << '#';
    }
    cout << endl;
    h--;
  }

  return 0;
}