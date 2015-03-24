#include<bits/stdc++.h>
using namespace std;

 int main()
 {
 	long int t;
 	scanf("%ld",&t);
 	long long int ans = 0,k;
 	while(t--)
 	{
 		scanf("%lld",&k);
 		ans ^= k;
 	}
 	printf("%lld",ans);
 	return 0;
 }
