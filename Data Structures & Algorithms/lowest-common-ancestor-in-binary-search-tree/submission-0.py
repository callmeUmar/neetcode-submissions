class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        cur = root
        
        while cur:
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            elif cur.val < q.val and cur.val < p.val:
                cur = cur.right
            else:
                return cur
            
