// Definition for singly-linked list.
#include <unordered_set>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        std::unordered_set<ListNode *> seen;
        for (ListNode *node = head; node != nullptr; node = node->next) {
            if (seen.count(node)) {
                return true;
            }
            seen.insert(node);
        }
        return false;
    }
};
