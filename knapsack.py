class Solution:
    def __init__(self):
        self.dp = []

    # Recursive + Memoization
    def solve(self, val, wt, capacity, i):
        if i == 0:
            return val[0] if wt[0] <= capacity else 0

        if self.dp[i][capacity] != -1:
            return self.dp[i][capacity]

        take = 0
        if wt[i] <= capacity:
            take = val[i] + self.solve(val, wt, capacity - wt[i], i - 1)

        skip = self.solve(val, wt, capacity, i - 1)
        self.dp[i][capacity] = max(take, skip)
        return self.dp[i][capacity]

    # Bottom-Up Tabulation
    def solveBottomUp(self, val, wt, capacity):
        n = len(val)
        dp = [[0] * (capacity + 1) for _ in range(n)]

        for w in range(capacity + 1):
            dp[0][w] = val[0] if wt[0] <= w else 0

        for i in range(1, n):
            for c in range(capacity + 1):
                take = val[i] + dp[i - 1][c - wt[i]] if wt[i] <= c else 0
                skip = dp[i - 1][c]
                dp[i][c] = max(take, skip)

        return dp[n - 1][capacity]

    # Space Optimized DP
    def solveSpaceOptimized(self, val, wt, capacity):
        n = len(val)
        prev = [0] * (capacity + 1)

        for w in range(capacity + 1):
            if wt[0] <= w:
                prev[w] = val[0]

        for i in range(1, n):
            curr = [0] * (capacity + 1)
            for c in range(capacity + 1):
                take = val[i] + prev[c - wt[i]] if wt[i] <= c else 0
                skip = prev[c]
                curr[c] = max(take, skip)
            prev = curr

        return prev[capacity]

    # Main knapsack function
    def knapsack(self, W, val, wt):
        # Recursive + Memoization version
        # n = len(val)
        # self.dp = [[-1] * (W + 1) for _ in range(n)]
        # return self.solve(val, wt, W, n - 1)

        # Bottom-Up version
        # return self.solveBottomUp(val, wt, W)

        # Space optimized version
        return self.solveSpaceOptimized(val, wt, W)


# Example usage
if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50

    sol = Solution()
    print(sol.knapsack(W, val, wt))  # Output: 220
