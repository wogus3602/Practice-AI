#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int N, K;
	int a[101];
	int dp[100001];

	scanf("%d %d", &N, &K);
	fill(dp, dp + 100001, 10000);
	dp[0] = 0;
	for (int i = 0; i < N; i++) {
		scanf("%d", &a[i]);
	}

	for (int i = 0; i < N; i++) {
		for (int j = a[i]; j <= K; j++) {
			dp[j] = min(dp[j], dp[j - a[i]] + 1);
		}
	}
	if (dp[K] == 10000) dp[K] = -1;
	printf("%d", dp[K]);
	
}