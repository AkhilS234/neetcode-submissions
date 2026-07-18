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
    int result = 1;
    std::stack<int> myStack;
public:
    int goodNodes(TreeNode* root) {

        myStack.push(root->val);
        dfs(root->left);
        while (!myStack.empty()) {
            myStack.pop();
        }
        myStack.push(root->val);
        dfs(root->right);
        return result;
    }
private:
    void dfs(TreeNode* node) {
        if(!node) {
            return;
        }
        if (node->val >= myStack.top()) {
            result += 1;
            myStack.push(node->val);
            dfs(node->left);
            dfs(node->right);
            myStack.pop();

        } else {
            dfs(node->left);
            dfs(node->right);
        }
    }
};
