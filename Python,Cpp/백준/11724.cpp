#include<iostream>
#include<vector>
using namespace std;

int check[1001] = { 0 };
vector<int> v[1001];

void dfs(int start) {
	if (check[start]) return;
	check[start] = 1;

	for (int i = 0; i < v[start].size(); i++) {
		int y = v[start][i];
		if (!check[y]) {
			dfs(y);
		}
	}
}

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	int N, M;
	int start, end;
	int count = 0;

	cin >> N >> M;

	for (int i = 0; i < M; i++) {
		cin >> start >> end;
		v[start].push_back(end);
		v[end].push_back(start);
	}
	for (int j = 1; j <= N; j++) {
		if (!check[j]) {
			dfs(j);
			count++;
		}
	}
	cout << count;

}