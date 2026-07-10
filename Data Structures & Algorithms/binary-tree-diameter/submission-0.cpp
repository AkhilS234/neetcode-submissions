/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
    int result = 0;
public:
    int diameterOfBinaryTree(TreeNode* root) {
        subTreeDepth(root);
        return result;
    }
private:
    int subTreeDepth(TreeNode* node) {
        if (!node) return 0;
        int leftDepth = subTreeDepth(node->left);
        int rightDepth = subTreeDepth(node->right);
        result = max(result, leftDepth+rightDepth);
        return 1 + max(leftDepth, rightDepth);
    }
};
