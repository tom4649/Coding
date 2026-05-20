/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
  public:
    ListNode *deleteDuplicates(ListNode *head) {
        ListNode dummy = ListNode(0, head);
        ListNode *node = &dummy;
        while (node->next) {
            if (node->next->next && node->next->val == node->next->next->val) {
                int duplicated = node->next->val;
                while (node->next && node->next->val == duplicated) {
                    node->next = node->next->next;
                }
            }
            else {
                node = node->next;
            }
        }
        return dummy.next;
    }
};
