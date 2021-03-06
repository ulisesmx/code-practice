def get_lower_common_ancestor(node, p, q):
    """ Left child """
    if p.val < node.val and q.val < node.val:
        return get_lower_common_ancestor(node.left, p, q)

    """ Right child """
    if node.val < p.val and node.val < q.val:
        return get_lower_common_ancestor(node.right, p, q)

    """ It is current level """
    return node

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return get_lower_common_ancestor(root, p, q)


    def lowestCommonAncestor_better(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                return node
        return None
