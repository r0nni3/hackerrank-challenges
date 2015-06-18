#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int solveMeSecond(int a, int b) {
  return a+b;
}

int main() {
  int t, num1, num2, sum;
  cin >> t;

  while(t-- > 0) {
    cin >> num1 >> num2;
    sum = solveMeSecond(num1,num2);
    cout << sum << endl;
  }

  return 0;
}
