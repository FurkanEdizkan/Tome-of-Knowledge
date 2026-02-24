class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        dp, mask = [[0]*n for _ in range(k)] + [[1]*n], (1<<t) - 1
        for i in range(k):
            for u,v,w in edges:
                dp[i][v] |= dp[i-1][u] << w & mask

        return max(map(int.bit_length, dp[k-1])) - 1