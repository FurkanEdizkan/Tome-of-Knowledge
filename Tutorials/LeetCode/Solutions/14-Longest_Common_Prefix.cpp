#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        
        string prefix = "";
        
        for (int i = 0; i < strs[0].length(); i++) {
            char c = strs[0][i];
            
            for (int j = 1; j < strs.size(); j++) {
                if (i >= strs[j].length() || strs[j][i] != c) {
                    return prefix;
                }
            }
            
            prefix += c;
        }
        
        return prefix;
    }
};

int main() {
    Solution sol;
    
    vector<string> test1 = {"flower", "flow", "flight"};
    cout << "Test 1: " << sol.longestCommonPrefix(test1) << endl;
    
    vector<string> test2 = {"dog", "racecar", "car"};
    cout << "Test 2: " << sol.longestCommonPrefix(test2) << endl;
    
    return 0;
}