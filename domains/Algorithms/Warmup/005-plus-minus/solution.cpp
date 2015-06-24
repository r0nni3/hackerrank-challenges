#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  int n, val;
  float c[4] = {0};

  cin >> n;
  while(n > 0) {
    cin >> val;
    if(val < 0) c[0]++;
    else if(val == 0) c[1]++;
    else if(val > 0) c[2]++;
    c[3]++; 
    n--;
  }

  printf("%.4f\n", c[2]/c[3]);
  printf("%.4f\n", c[0]/c[3]);
  printf("%.4f\n", c[1]/c[3]);

  return 0;
}