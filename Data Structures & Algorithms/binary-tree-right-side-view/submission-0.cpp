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
public:
    vector<int> rightSideView(TreeNode* root) {
        
        std::vector<int> result;
        std::queue<TreeNode*> myQueue; 

        if (!root) {
            return result;
        }

        myQueue.push(root);

        while (myQueue.size() >= 1) {

            int size = myQueue.size();
            TreeNode* last;

            for (int i = 0; i < size; i++) {
                TreeNode* node = myQueue.front();

                if (node->left) {
                    myQueue.push(node->left);
                }

                if (node->right) {
                    myQueue.push(node->right);
                }
                last = node;
                myQueue.pop();
            }

            result.push_back(last->val);
        } 
        return result;
    }
};
