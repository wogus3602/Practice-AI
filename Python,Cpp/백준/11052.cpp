#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int N;
	int dp[10000] = {0};
	int P[10002];
	scanf("%d", &N);

	for (int i = 1; i <= N; i++) {
		scanf("%d", &P[i]);
	}
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= i; j++) {
			dp[i] = max(dp[i], dp[i-j]+P[j]);
		}
	}

	printf("%d", dp[N]);

}