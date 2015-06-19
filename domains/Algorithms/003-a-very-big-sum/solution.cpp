#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int sum(int a, int b) {
  return a+b;
}

int main() {
  int n;
  unsigned long sum = 0, value;

  cin >> n;
  while(n>0) {
  	cin >> value;
  	sum += value;
  	--n;
  }

  cout << sum << endl;

  return 0;
}