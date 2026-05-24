// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
  public:
    int kthSmallest(TreeNode *root, int k) {
        int k_th_smallest = -1;
        int num_seen = 0;
        auto traverse = [k, &k_th_smallest, &num_seen](auto &self, TreeNode *node) -> void {
            if (!node) {
                return;
            }
            self(self, node->left);
            if (k_th_smallest >= 0) {
                return;
            }
            num_seen++;
            if (num_seen== k){
                k_th_smallest = node->val;
                return;
            }
            self(self, node->right);
        };

        traverse(traverse, root);
        return k_th_smallest;
    }
};
