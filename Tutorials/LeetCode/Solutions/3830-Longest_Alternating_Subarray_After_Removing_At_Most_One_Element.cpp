class Solution {
public:
    int longestAlternating(vector<int>& nums) {
        int n = nums.size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(2, vector<int>(2, 1)));
        int ans = 1;
        for (int i=1; i<n; i++){
            if (nums[i-1]>nums[i]) {
                dp[i][0][0] = dp[i-1][1][0] + 1;
                dp[i][0][1] = dp[i-1][1][1] + 1;
            }

            if (nums[i-1] < nums[i]) {
                dp[i][1][0] = dp[i-1][0][0] + 1;
                dp[i][1][1] = dp[i-1][0][1] + 1;
            }

            if (i >= 2) {
                if (nums[i] < nums[i-2]) {
                    dp[i][0][1] = max(dp[i][0][1], dp[i-2][1][0] + 1);
                }
                if (nums[i] > nums[i-2]){
                    dp[i][1][1] = max(dp[i][1][1], dp[i-2][0][0] + 1);
                }
            }
            ans = max(ans, max({dp[i][0][0], dp[i][0][1], dp[i][1][0], dp[i][1][1]})); 
        }
        return ans;
    }
};