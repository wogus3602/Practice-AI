#include<iostream>
using namespace std;

long long dp[91];

long long topDown(int N) {
	if (N == 1 || N == 2) return 1;
	if (dp[N] != 0) return dp[N];
	return dp[N] = topDown(N-1) + topDown(N-2);
}

int main() {
	int N;
	scanf("%d", &N);
	//topDown(N);
	printf("%lld", topDown(N));
}


////Bottom up
//int main() {
//	int N;
//	long long dp[91];
//	scanf("%d", &N);
//
//	dp[1] = 1;
//	dp[2] = 1;
//
//	for (int i = 3; i <= N; i++) {
//		dp[i] = dp[i - 1] + dp[i - 2];
//	}
//
//	printf("%lld", dp[N]);
//
//	return 0;
//}