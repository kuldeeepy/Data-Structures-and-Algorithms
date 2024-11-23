class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# (Question 1)
def count_nodes(root):
    if root == None: return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# Example Input
root = TreeNode(1, 
                TreeNode(2, 
                         TreeNode(4), 
                         TreeNode(5)),
                TreeNode(3))

# Example Output
# print(count_nodes(root))  # Expected Output: 5 


# (Question 2)
def find_max(root):
    if root == None: return -1

    left_max = find_max(root.left)
    right_max = find_max(root.right)
    return max(root.value, left_max, right_max)


# Example Input
root = TreeNode(1, 
                TreeNode(2, 
                         TreeNode(4), 
                         TreeNode(5)),
                TreeNode(3))

# Example Output
# print(find_max(root))  # Expected Output: 5 


# (Question 3)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Example Input
root = TreeNode(1, 
                TreeNode(2, 
                         TreeNode(4), 
                         TreeNode(5)),
                TreeNode(3))

# Example Output
# print(inorder_traversal(root))  # Expected Output: [4, 2, 5, 1, 3] 


# (Question 4)
def is_symmetric(root):

    if root == None: return True

    def check_symmetric(t1, t2):

        if not t1 and not t2:
            return True
        
        if not t1 or not t2:
            return False
        return (t1.value == t2.value) and check_symmetric(t1.left, t2.right) and check_symmetric(t1.right, t2.left)
    
    return check_symmetric(root.left, root.right)

# Example Input
root = TreeNode(1, 
                TreeNode(2, 
                         TreeNode(3), 
                         TreeNode(4)),
                TreeNode(2, 
                         TreeNode(4), 
                         TreeNode(3)))

# Example Output
# print(is_symmetric(root))  # Expected Output: True 


# (Question 5)
def tree_height(root):
    if root == None: return -1

    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    return 1 + max(left_height, right_height)



# Example Input
root = TreeNode(1, 
                TreeNode(2, 
                         TreeNode(4), 
                         TreeNode(5)),
                TreeNode(3))

# Example Output
# print(tree_height(root))  # Expected Output: 2 

def findMinValue(root):
    while root.left is not None:
        root = root.left
    return root.value

# Example usage:

root = TreeNode(50, 
                TreeNode(30, 
                         TreeNode(70), 
                         TreeNode(20)),
                TreeNode(40, 
                         TreeNode(60), 
                         TreeNode(80)))

result = findMinValue(root)
print(result)


