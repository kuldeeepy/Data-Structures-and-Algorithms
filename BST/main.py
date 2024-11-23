class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Binary Search Tree Insertion 
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, data):

#         if self.root == None:
#             self.root = Node(data)
#         else:
#             self.insert_recursively(self.root, data)

#     def insert_recursively(self, node, data):

#         if data < node.data:
#             if node.left == None:
#                 node.left = Node(data)
#             else:
#                 self.insert_recursively(node.left, data)

#         elif data > node.data:
#             if node.right == None:
#                 node.right = Node(data)
#             else:
#                 self.insert_recursively(node.right, data)

#     def print_tree(self):
#         if self.root:
#             self.print_recursively(self.root)

#     def print_recursively(self, node):

#         if node:
#             self.print_recursively(node.left)
#             print(node.data, end=" ")
#             self.print_recursively(node.right)

def print_tree(root):
    """Helper function to print the tree in inorder traversal (sorted order)."""
    if root is not None:
        print_tree(root.left)
        print(root.value, end=" ")
        print_tree(root.right)

# (Question 1)
def search_BST(root, val):
    if root == None: return False

    if root.value == val:
        return True
    if root.value < val:
        return search_BST(root.right, val)
    else:
        return search_BST(root.left, val)

# Example Input
root = TreeNode(8, 
                TreeNode(3, 
                         TreeNode(1), 
                         TreeNode(6, TreeNode(4), TreeNode(7))),
                TreeNode(10, 
                         None, 
                         TreeNode(14, TreeNode(13))))

# print(search_BST(root, 6))  # Expected Output: True
# print(search_BST(root, 15)) # Expected Output: False 


# (Question 2)
def insert_BST(root, val):

    if root == None:
        return TreeNode(val)
    
    if root.value < val:
        root.right = insert_BST(root.right, val)
    elif root.value > val:
        root.left = insert_BST(root.left, val)
    return root

# Example Input
root = TreeNode(8, 
                TreeNode(3, 
                         TreeNode(1), 
                         TreeNode(6, TreeNode(4), TreeNode(7))),
                TreeNode(10, 
                         None, 
                         TreeNode(14, TreeNode(13))))

# Example Output
new_root = insert_BST(root, 5)
# print_tree(new_root) 
# Expected Output: 5 will be inserted as the left child of 6


# (Question 3)
def find_min_BST(root):
    if root == None: return None

    while root.left:
        root = root.left
    return root.value

# Example Input
root = TreeNode(8, 
                TreeNode(3, 
                         TreeNode(1), 
                         TreeNode(6, TreeNode(4), TreeNode(7))),
                TreeNode(10, 
                         None, 
                         TreeNode(14, TreeNode(13))))

# Expected Output
# print(find_min_BST(root))  # Expected Output: 1


# (Question 3)
def find_max_BST(root):
    if root == None: return None

    while root.right:
        root = root.right
    return root.value

# Example Input
root = TreeNode(8, 
                TreeNode(3, 
                         TreeNode(1), 
                         TreeNode(6, TreeNode(4), TreeNode(7))),
                TreeNode(10, 
                         None, 
                         TreeNode(14, TreeNode(13))))

# Expected Output
# print(find_max_BST(root))  # Expected Output: 14 


# (Question 4)
def insert_BST(root, val):
    node = TreeNode(val)

    parent = None
    current = root
    while current != None:
        parent = current
        if val == current.value:
            return
        if val < current.value:
            current = current.left
        else:
            current = current.right
    if val < parent.value:
        parent.left = node
    else:
        parent.right = node
    return root

# Example Input
root = TreeNode(8, 
                TreeNode(3, 
                         TreeNode(1), 
                         TreeNode(6, TreeNode(4), TreeNode(7))),
                TreeNode(10, 
                         None, 
                         TreeNode(14, TreeNode(13))))

# Example Output
new_root = insert_BST(root, 5)
# print_tree(new_root)
# Expected Output: 5 will be inserted as the left child of 6


# (Question 5)
def delete_BST(root, key):
    if root == None: return None

    if root.value == key: # If root is equal to key
        if not root.left: # If no left child return right child
            return root.right
        
        if not root.right: # If no right child return left child
            return root.left
        
        temp = root.right
        while temp.left: # Find inorder successor (leftmost child of right subtree)
            temp = temp.left
        root.value = temp.value # replace with root
        root.right = delete_BST(root.right, root.value) # delete the successor
    elif root.value > key: # if key is smaller
        root.left = delete_BST(root.left, key)
    else: # if key is bigger
        root.right = delete_BST(root.right, key)
    return root

# Example Input
root = TreeNode(8, 
                TreeNode(3, 
                         TreeNode(1), 
                         TreeNode(6, TreeNode(4), TreeNode(7))),
                TreeNode(10, 
                         None, 
                         TreeNode(14, TreeNode(13))))

# Expected Output
new_root = delete_BST(root, 6)
# print_tree(new_root)


# (Question 6)
def bstToGst(root):
    def inOrderR(node):
        nonlocal cSum
        if node == None:
            return
        
        inOrderR(node.right)
        cSum += node.value
        node.value = cSum
        inOrderR(node.left)
        
    cSum = 0
    inOrderR(root)
    return root


# Example Input
root = TreeNode(4, 
                TreeNode(2, 
                         TreeNode(1), 
                         TreeNode(3)),
                TreeNode(6, 
                         TreeNode(5), 
                         TreeNode(7)))

# Expected Output
new_root = bstToGst(root)
# print_tree(new_root)


# (Question 7)
def merge_BSTs_to_list(root1, root2):
    def merge1(node, arr):
        if node == None:
            return arr
        merge1(node.left, arr)
        arr.append(node.value)
        merge1(node.right, arr)
        return arr
    
    list1, list2 = [], []
    merge1(root1, list1)
    merge1(root2, list2)
    
    merged_list = []
    i,j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i+= 1
        else:
            merged_list.append(list2[j])
            j+= 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list

# Example Input
root1 = TreeNode(4, 
                 TreeNode(2, TreeNode(1), TreeNode(3)), 
                 TreeNode(6, TreeNode(5), TreeNode(7)))

root2 = TreeNode(10, 
                 TreeNode(8, TreeNode(7), TreeNode(9)), 
                 TreeNode(12, None, TreeNode(14)))

merged_list = merge_BSTs_to_list(root1, root2)
# print(merged_list)
# Expected Output
# [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 12, 14] 

