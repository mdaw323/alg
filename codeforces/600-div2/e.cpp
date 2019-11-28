#include<stdio.h>

int min(int a,int b) {
	if (a>b) {
		return b;
	} else {
		return a;
	}
}

int max(int a,int b) {
	if (a<b) {
		return b;
	} else {
		return a;
	}
}

int main() {
	int n,m,x,s;
	scanf("%d%d",&n,&m);
	int A[m+1], B[m+1], dp[m+1];
	
	for (int i = 1; i<=n; i++) {
		scanf("%d%d", &x, &s);
		A[i] = x-s >0 ? x-s :0;
		B[i] = x+s >m ? m : x+s;
	}
	
	for (int p = 1; p<=m; p++) {
		dp[p] = 999999999;
	}
	dp[0] = 0;	
	for (int p = 1; p<=m; p++) {
		for (int i = 1; i<=n; i++) {
			int a = A[i];
			int b = B[i];
			if (p >= a && p <= b) {
				dp[p] = dp[p-1];				
			} else if (p < a) {
				int pwr = a - p;
				dp[p] = min(dp[p], min(pwr + dp[max(0,a-pwr-1)], p));
			} else if ( p > b) {
				int pwr = p - b;
				dp[p] = min(dp[p], min(pwr + dp[max(a-pwr-1,0)], p));
			}
		}
	}
	printf("%d",dp[m]);
	return 0;
}

