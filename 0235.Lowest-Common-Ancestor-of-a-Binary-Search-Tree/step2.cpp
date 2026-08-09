// Definition for a binary tree node.
#include <algorithm>
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
  public:
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q) {
        int smaller = std::min(p->val, q->val);
        int larger = std::max(p->val, q->val);
        TreeNode *node = root;
        while (node) {
            if (smaller <= node->val && node->val <= larger) {
                return node;
            }
            if (node->val < smaller) {
                node = node->right;
                continue;
            }
            if (node->val > larger) {
                node = node->left;
                continue;
            }
        }
        return nullptr;
    }
};
