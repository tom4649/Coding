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
        ListNode *tail = &dummy;
        ListNode *node = dummy.next;
        while (node && node->next) {
            if (node->val != node->next->val){
                tail = tail->next;
                node = node->next;
                continue;
            }
            while (node->next && node->val == node->next->val){
                node = node->next;
            }
            tail->next = node->next;
            node = node->next;
        }
        return dummy.next;
    }
};
