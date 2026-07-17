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
    vector<vector<int>> levelOrder(TreeNode* root) {
        
        std::vector<vector<int>> result;

        if (!root) {
            return result;
        }

        std::queue<TreeNode*> myQueue;

        myQueue.push(root);

        while (myQueue.size() >= 1) {
            int size = myQueue.size();
            std::vector<int> row;
            for (int i = 0; i < size; i++) {
                TreeNode* node = myQueue.front();
                myQueue.pop();
                row.push_back(node->val);
                if (node->left) {
                    myQueue.push(node->left);
                }
                if (node->right) {
                    myQueue.push(node->right);
                }
            }

            if (row.size() > 0) {
                result.push_back(row);
            }
        }
        return result;
    }
};
