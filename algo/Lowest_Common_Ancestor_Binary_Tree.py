# Lowest Common Ancestor in a Binary Search Tree
# common Node of two node
"""
ALGO:

lca(root, n1, n2){
if root==None: return Null
if root==n1 and root==n2: return n2
left=lca(root, n1, n2)
right=lca(root, n1, n2)
if(left!=None and right!= None): return root
if(left==None and right== None): return None
return left if left!=None else right

}
"""


# n1 and n2

# A Binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def lca(root, n1, n2):
    # Base Case
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if root.data > n1 and root.data > n2:
        return lca(root.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if root.data < n1 and root.data < n2:
        return lca(root.right, n1, n2)

    return root


# Let us construct the BST shown in the figure

if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    n1 = 10
    n2 = 14
    t = lca(root, n1, n2)
    print("LCA of %d and %d is %d" % (n1, n2, t.data))