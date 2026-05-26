
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
  public:
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q) {
        if (root == nullptr) {
            return nullptr;
        }
        if (root == p || root == q) {
            return root;
        }
        TreeNode *left_found = lowestCommonAncestor(root->left, p, q);
        TreeNode *right_found = lowestCommonAncestor(root->right, p, q);
        if (left_found == nullptr) {
            return right_found;
        }
        if (right_found == nullptr) {
            return left_found;
        }
        return root;
    }
};
