#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy(0);
        ListNode* cur = &dummy;
        
        // Merge by comparing nodes from both lists
        while (list1 && list2) {
            if (list1->val <= list2->val) {
                cur->next = list1;
                list1 = list1->next;
            } else {
                cur->next = list2;
                list2 = list2->next;
            }
            cur = cur->next;
        }
        
        // Attach remaining nodes (one list will be empty)
        cur->next = list1 ? list1 : list2;
        
        return dummy.next;
    }
};

// Helper: build list from vector
ListNode* fromVector(vector<int>& arr) {
    if (arr.empty()) return nullptr;
    ListNode* head = new ListNode(arr[0]);
    ListNode* cur = head;
    for (int i = 1; i < arr.size(); i++) {
        cur->next = new ListNode(arr[i]);
        cur = cur->next;
    }
    return head;
}

// Helper: convert list to vector for easy comparison
vector<int> toVector(ListNode* head) {
    vector<int> res;
    while (head) {
        res.push_back(head->val);
        head = head->next;
    }
    return res;
}

// Helper: print vector
void printVector(const vector<int>& v) {
    cout << "[";
    for (int i = 0; i < v.size(); i++) {
        if (i > 0) cout << ",";
        cout << v[i];
    }
    cout << "]";
}

int main() {
    Solution sol;
    
    struct Test {
        vector<int> list1;
        vector<int> list2;
        vector<int> expected;
    };
    
    vector<Test> tests = {
        {{1, 2, 4}, {1, 3, 4}, {1, 1, 2, 3, 4, 4}},
        {{}, {}, {}},
        {{}, {0}, {0}},
        {{1, 3, 5}, {2, 4, 6}, {1, 2, 3, 4, 5, 6}},
    };
    
    for (const auto& t : tests) {
        ListNode* l1 = fromVector((vector<int>&)t.list1);
        ListNode* l2 = fromVector((vector<int>&)t.list2);
        ListNode* result = sol.mergeTwoLists(l1, l2);
        vector<int> res = toVector(result);
        
        string status = res == t.expected ? "✓" : "✗";
        cout << status << " mergeTwoLists(";
        printVector(t.list1);
        cout << ", ";
        printVector(t.list2);
        cout << ") = ";
        printVector(res);
        cout << " (expected ";
        printVector(t.expected);
        cout << ")" << endl;
    }
    
    return 0;
}