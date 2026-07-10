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
    bool isBalanced(TreeNode* root) {
        if (!root) {
            return true;
        }
        treeDepth(root);
        if (result <= 1) {
            return true;
        }
        else {
            return false;
        }
    }
private: 
    int treeDepth(TreeNode* node) {
        if (!node) return 0;
        int left = treeDepth(node->left);
        int right = treeDepth(node->right);
        
        result = max(result, abs(left-right));
        return 1 + max(left, right);
    }
};
