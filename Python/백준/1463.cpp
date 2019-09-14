#include<iostream>
#include<algorithm>
using namespace std;
const int MAX = 1000000;

int dp[MAX + 1];

int makeOne(int N) {
	
	if (N == 1) return 0;
	if (dp[N] != 0) return dp[N];

	dp[N] = makeOne(N-1) + 1;
	if (N % 3 == 0) dp[N] = min(dp[N],makeOne(N / 3) + 1);
	if (N % 2 == 0) dp[N] = min(dp[N], makeOne(N / 2) + 1);

	return dp[N];
}
//Top down
int main() {
	int N;
	scanf("%d", &N);
	
	printf("%d", makeOne(N));
}

////Bottom up
//int main() {
//	int N;
//	scanf("%d", &N);
//
//	dp[1] = 0;
//	dp[2] = 1;
//
//	for (int i = 3; i <= N; i++) {
//		dp[i] = dp[i - 1] + 1;
//		if (i % 3 == 0) dp[i] = min(dp[i], dp[i / 3] + 1);
//		if (i % 2 == 0) dp[i] = min(dp[i], dp[i / 2] + 1);
//	}
//	printf("%d", dp[N]);
//}