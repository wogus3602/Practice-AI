#include <iostream>
#define mod 1000000000

using namespace std;
int DP[101][10];

int main() {
	int N;
	long long sum = 0;

	for (int i = 1; i <= 9; ++i) {        //1일 때 초기화 -> 2부터 동적으로 구할 수 있음
		DP[1][i] = 1;
	}

	cin >> N;

	for (int i = 2; i <= N; ++i) {
		for (int j = 0; j <= 9; ++j) {
			if (j == 0) DP[i][j] = DP[i - 1][j + 1];            //1에서만 올 수 있음
			else if (j == 9) DP[i][j] = DP[i - 1][j - 1];        //8에서만 올 수 있음
			else DP[i][j] = (DP[i - 1][j - 1] + DP[i - 1][j + 1]) % mod;    //양쪽에서 올 수 있음
		}
	}

	for (int i = 0; i <= 9; ++i) sum += DP[N][i];            //총 경우의 수

	cout << sum % mod << endl;

	return 0;
}

