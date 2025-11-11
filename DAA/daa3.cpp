#include <bits/stdc++.h>
using namespace std;

int knapsack(int capacity, const vector<int>& weights, const vector<int>& values, int n) {
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));

    // Build the DP table
    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= capacity; w++) {
            if (weights[i - 1] <= w)
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]]);
            else
                dp[i][w] = dp[i - 1][w];
        }
    }

    return dp[n][capacity];
}

int main() {
    int n, capacity;

    cout << "Enter number of items: ";
    cin >> n;

    cout << "Enter capacity of knapsack: ";
    cin >> capacity;

    vector<int> weights(n), values(n);

    cout << "Enter weights of items:\n";
    for (int i = 0; i < n; i++)
        cin >> weights[i];

    cout << "Enter values of items:\n";
    for (int i = 0; i < n; i++)
        cin >> values[i];

    int max_value = knapsack(capacity, weights, values, n);

    cout << "The maximum value that can be obtained is: " << max_value << endl;

    return 0;
}
