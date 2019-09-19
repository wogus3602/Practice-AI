#include<iostream>
using namespace std;
int main() {
	long long dp[1001][10] = { 0 };
	int N, Sum = 0;
	cin >> N;

	for (int i = 0; i < 10; i++) dp[1][i] = 1;

	for (int i = 2; i <= N; i++) {
		for (int j = 0; j < 10; j++) {
			for (int k = j; k < 10; k++) {
				dp[i][j] += dp[i - 1][k];
			}
			dp[i][j] %= 10007;
		}
	}

	for (int i = 0; i < 10; i++) Sum += dp[N][i];
	cout << Sum % 10007;
}