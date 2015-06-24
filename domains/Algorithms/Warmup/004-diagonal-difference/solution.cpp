#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  int n,i,j,value,sum=0;

  cin >> n;
  std::vector< std::vector<int> > v(n);
  for(i=0; i<n; ++i){
  	for(j=0; j<n; ++j) {
  		cin >> value; 
  		v[i].push_back(value);
  	}
  }

  for (i=0, j=n-1; i<n && j>=0; i++, j--) {
  	sum += v[i][i];
  	sum -= v[j][i];
  }
  sum = (sum < 0) ? sum*-1 : sum;
  cout << sum << endl;

  return 0;
}